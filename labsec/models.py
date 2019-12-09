#Django
from django.db import models

class Certificado(models.Model):

    class Meta:
        db_table = 'certificados'

    country = models.CharField(
        max_length=2,
        default='',
        blank=False,
        null = False,
    )

    state = models.CharField(
        max_length=255,
        default='',
        blank=False,
        null = False,
    )

    locality = models.CharField(
        max_length=255,
        default='',
        blank=False,
        null = False,
    )

    organization = models.CharField(
        max_length=255,
        default='',
        blank=False,
        null = False,
    )

    organizationalUnit = models.CharField(
        max_length=255,
        default='',
        blank=True,
        null = False,
    )

    certificateName = models.CharField(
        max_length=255,
        default='',
        blank=False,
        null = False,
    )

    serialNumber = models.IntegerField(
        default=0
    )


class Chaves(models.Model):
    class Meta:
        db_table = 'chaves'

    tipo = models.IntegerField(
    )

    n = models.CharField(
        max_length=650
    )

    e = models.CharField(
        max_length=650
    )

    p = models.CharField(
        max_length=650
    )

    q = models.CharField(
        max_length=650
    )

    d = models.CharField(
        max_length=650
    )

class Resumo(models.Model):

    class Meta:
        db_table = 'resumo'

    nameUpload = models.CharField(
        max_length=200
    )
    resumoCriptografico = models.CharField(
        max_length=64
    )

    arquivo = models.FileField(
        blank=True,
        default='',
        upload_to='files'
    )