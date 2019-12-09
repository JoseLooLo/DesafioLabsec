#Django
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

#Project
from . import views
from .views import ResumoList, ChavesList, GerarCertificado, listaCertificados, CertificadoList

app_name = "website"

urlpatterns = [
    path('', views.indexFunction, name = 'index'),
    path('exemplos/', views.exemplosFunction, name = 'exemplos'),
    path('getresumo/', ResumoList.as_view(), name='resumo-list'),
    path('resumo/', views.resumoFunction, name = "resumo"),
    path('erros/', views.erroFunction, name = "erro"),
    path('chaves/', views.gerarChaves, name = "chaves"),
    path('getchaves/', ChavesList.as_view(), name='chaves-list'),
    path('getcertificados/', CertificadoList.as_view(), name='certificado-list'),
    path('gerarcertificado/', GerarCertificado.as_view(), name = "gerarcertificado"),
    path('gerarcertificado/raiz', views.gerarCertificadoRaiz, name = "gerarcertificadoraiz"),
    path('certificados/', listaCertificados.as_view(), name = "certificados"),
]
