#Django
from rest_framework import serializers

#Project
from .models import Resumo, Chaves, Certificado

class ResumoSerializer(serializers.ModelSerializer):

    class Meta:

        model = Resumo
        fields = ('nameUpload', 'resumoCriptografico', 'arquivo',)
        read_only_fields = ('nameUpload', 'resumoCriptografico',)
        write_only_fields = ('arquivo',)

class ChavesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Chaves
        fields = ('tipo', 'n', 'e', 'p', 'q', 'd',)
        read_only_fields = ('n', 'e', 'p', 'q', 'd',)

class CertificadosSerializer(serializers.ModelSerializer):

    class Meta:

        model = Certificado
        fields = ('serialNumber', 'certificateName', 'organization', 'organizationalUnit', 'country', 'locality', 'state')

class CertificadoRaizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Certificado
        exclude = ('serialNumber', 'certificateName', 'organization', 'organizationalUnit', 'country', 'locality', 'state')