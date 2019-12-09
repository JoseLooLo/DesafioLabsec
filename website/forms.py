#Django
from django import forms

#Project
from labsec.models import Certificado

class InsereCertificadoForm(forms.ModelForm):

    class Meta:
        model = Certificado

        fields = [
            'serialNumber',
            'certificateName',
            'organization',
            'organizationalUnit',
            'country',
            'locality',
            'state'
        ]