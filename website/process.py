#Others
import hashlib
import os
from random import randint
from Crypto.PublicKey import RSA
from OpenSSL import crypto, SSL
from socket import gethostname

def upload_to_sha256(arquivo):

    buffer_size = 1024
    sha = hashlib.sha256()

    with open(arquivo, 'rb') as arq:
        while True:
            data = arq.read(buffer_size)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest()

def deletefile(arquivo):
    os.remove(arquivo)

def gerarCertificadoRaiz():
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    certificado = crypto.X509()
    certificado.get_subject().C = "BR"
    certificado.get_subject().ST = "Santa Catarina"
    certificado.get_subject().L = "Florianopolis"
    certificado.get_subject().O = "UFSC"
    certificado.get_subject().OU = "-"
    certificado.get_subject().CN = gethostname()
    certificado.set_serial_number(333)
    certificado.gmtime_adj_notBefore(0)
    certificado.gmtime_adj_notAfter(315360000)
    certificado.set_issuer(certificado.get_subject())

    certificado.set_pubkey(key)
    certificado.sign(key, 'sha256')

    if os.path.exists("CertificadoACRAIZ.crt"):
        print ("Certificado existente.")
    else:
        open("CertificadoACRAIZ.crt", 'wb').write(crypto.dump_certificate(crypto.FILETYPE_PEM, certificado))
        open("PrivateKeyACRAIZ.key", 'wb').write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    

def gerarCertificado(name, serial, state, country, locality, org, orgunit):
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    certificado = crypto.X509()
    certificado.get_subject().C = country
    certificado.get_subject().ST = state
    certificado.get_subject().L = locality
    certificado.get_subject().O = org
    certificado.get_subject().OU = orgunit
    certificado.get_subject().CN = name
    certificado.set_serial_number(int(serial))
    certificado.gmtime_adj_notBefore(0)
    certificado.gmtime_adj_notAfter(200000000)

    try:
        certRaiz = crypto.load_certificate(crypto.FILETYPE_PEM, open("CertificadoACRAIZ.crt").read())
    except:
        print("Certificado raiz não encontrado")
        return -1
    
    try:
        privatekeyRaiz = crypto.load_privatekey(crypto.FILETYPE_PEM, open("PrivateKeyACRAIZ.key").read())
    except:
        print("Private key raiz não encontrada")
        return -2
    certificado.set_issuer(certRaiz.get_subject())

    certificado.set_pubkey(key)
    certificado.sign(privatekeyRaiz, 'sha256')

    open("certificates/{}{}.crt".format(name, serial), 'wb').write(crypto.dump_certificate(crypto.FILETYPE_PEM, certificado))
    open("certificates/{}{}.key".format(name, serial), 'wb').write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))

def gerarRSAkey(tipo):
    rand = 0
    while (rand % 2 == 0):
        rand = randint(65537, 100000)
    key = RSA.generate(tipo, e=rand)
    return key