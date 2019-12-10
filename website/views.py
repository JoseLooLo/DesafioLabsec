#Django
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.core.files.storage import FileSystemStorage
from rest_framework import generics, status
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.template import RequestContext

#Project
from . import process
from labsec.models import Resumo, Chaves, Certificado
from labsec.serializer import ResumoSerializer, ChavesSerializer, CertificadosSerializer
from .forms import InsereCertificadoForm
from . import db

#Others
import json

#------------------------------------#
'''Erros do Site'''
#------------------------------------#

def handler404(request, *args, **argv):
    response = render(request, 'website/404.html')
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render(request, 'website/500.html')
    response.status_code = 500
    return response

#------------------------------------#
'''Funções do Site'''
#------------------------------------#

def indexFunction(request):
    return render(request, "website/index.html")

def exemplosFunction(request):
    return render(request, "website/exemplos.html")

def erroFunction(request):
    return render(request, "website/erros.html")

def resumoFunction(request):
    contexto = {
        'texto': "Envie um documento para obter seu Resumo Criptográfico",
        'desativado': "true"
    }
    try:
        if request.method == 'POST' and request.FILES['arquivo']:
            #Salva o arquivo em disco para usar no process
            storage = FileSystemStorage(location="files/")
            filename = storage.save(request.FILES['arquivo'].name, request.FILES['arquivo'])
            uploaded_file_url = storage.url(filename)
            up_to_sha = process.upload_to_sha256("files/"+uploaded_file_url)

            contexto = {
                'texto': up_to_sha,
                'ativo': "true"
            }
            try:
                db.insertResumo(filename, up_to_sha, "files/"+uploaded_file_url)
            except:
                print("coe")
    except:
        print("Nenhum arquivo")
    return render(request, "website/resumo.html", contexto)

def gerarChaves(request):
    contexto = {
        'linha_n': 1,
        'linha_e': 1,
        'linha_p': 1,
        'linha_q': 1,
        'linha_d': 1,
        'n': "",
        'e': "",
        'p': "",
        'q': "",
        'd': "",
    }
    if request.method == 'POST':
        key = process.gerarRSAkey(int(request.POST['optradio']))

        if (int(request.POST['optradio']) == 1024):
            contexto = {
                'linha_n': 4,
                'linha_e': 1,
                'linha_p': 2,
                'linha_q': 2,
                'linha_d': 4,
                'n': str(key.n),
                'e': str(key.e),
                'p': str(key.p),
                'q': str(key.q),
                'd': str(key.d), 
            }
        else:
            contexto = {
                'linha_n': 7,
                'linha_e': 1,
                'linha_p': 4,
                'linha_q': 4,
                'linha_d': 7,
                'n': str(key.n),
                'e': str(key.e),
                'p': str(key.p),
                'q': str(key.q),
                'd': str(key.d), 
            }
        
        try:
            db.insertChaves(int(request.POST['optradio']), str(key.n), str(key.e), str(key.p), str(key.q), str(key.d))
        except:
            print("coe")
        
    return render(request, "website/chaves.html", contexto)

def gerarCertificadoRaiz(request):
    if request.method == "POST":
        process.gerarCertificadoRaiz()
    
    #Volta para o index devido a problemas no formulário
    return render(request, "website/index.html")


#------------------------------------#
'''CLasses do Site'''
#------------------------------------#

class listaCertificados(ListView):
    template_name = "website/certificados.html"
    model = Certificado
    context_object_name = "certificados"

class GerarCertificado(CreateView):
    template_name = "website/gerarcertificado.html"
    model = Certificado
    form_class = InsereCertificadoForm
    success_url = reverse_lazy("website:certificados")

    def post(self, request):
        try:
            process.gerarCertificado(request.POST['certificateName'], request.POST['serialNumber'], request.POST['state'], request.POST['country'], request.POST['locality'], request.POST['organization'], request.POST['organizationalUnit'])
        except:
            print("Erro")
        return(super().post(request))

#------------------------------------#
'''CLasses da API'''
#------------------------------------#

class ResumoList(generics.ListCreateAPIView):
    
    queryset = Resumo.objects.all()
    serializer_class = ResumoSerializer
    
    def post(self, request):
        serializer = ResumoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.validated_data['nameUpload'] = request.FILES['arquivo'].name
            storage = FileSystemStorage()
            filename = storage.save(request.FILES['arquivo'].name, request.FILES['arquivo'])
            resumo = process.upload_to_sha256(filename)
            serializer.validated_data['resumoCriptografico'] = resumo
            process.deletefile(filename)
            serializer.save()
            retorno = {
                'nameUpload' : filename,
                'resumoCriptografico' : resumo
            }
            return Response(json.dumps(retorno, sort_keys=True, indent=4), status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

class ChavesList(generics.ListCreateAPIView):
    
    queryset = Chaves.objects.all()
    serializer_class = ChavesSerializer

    def post(self, request):
        serializer = ChavesSerializer(data=request.data)
        if serializer.is_valid():
            key = process.gerarRSAkey(int(request.data['tipo']))
            serializer.validated_data['n'] = str(key.n)
            serializer.validated_data['e'] = str(key.e)
            serializer.validated_data['p'] = str(key.p)
            serializer.validated_data['q'] = str(key.q)
            serializer.validated_data['d'] = str(key.d)
            serializer.save()
            retorno = {
                'tipo': int(request.data['tipo']),
                'n': str(key.n),
                'e': str(key.e),
                'p': str(key.p),
                'q': str(key.q),
                'd': str(key.d), 
            }
            return Response(json.dumps(retorno, sort_keys=True, indent=4), status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_400_BAD_REQUEST)

class CertificadoList(generics.ListCreateAPIView):

    queryset = Certificado.objects.all()
    serializer_class = CertificadosSerializer

    def post(self, request):
        serializer = CertificadosSerializer(data=request.data)
        if serializer.is_valid():
            process.gerarCertificado(request.POST['certificateName'], request.POST['serialNumber'], request.POST['state'], request.POST['country'], request.POST['locality'], request.POST['organization'], request.POST['organizationalUnit'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)