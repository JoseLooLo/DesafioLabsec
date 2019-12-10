===========
Observações
===========

É necessário possuir o python e o pip instalados previamente no sistema.
> Em alguns casos, como no windows, utilize o comando python no lugar de python3.
> Em alguns casos, se não funcionar, utilize o comando pip3 no lugar de pip.

==========
Instalação
==========

Para instalar as depêndencias necessárias, execute:

    pip install -r requisitos.txt

Ou instale manualmente os pacotes cujos nomes estão no arquivo requisitos.txt

============
Dependências
============

Após instalar as dependências e antes de executar o projeto, executar os seguintes comandos estando na pasta raiz do projeto.
Para configurações inicias e criação do banco de dados

    python3 manage.py makemigrations

Logo após executar para criar as tabelas

    python3 manage.py migrate

========
Execução
========

Para executar o projeto, executar o seguinte comando estando na pasta raiz do projeto.

    python3 manage.py runserver

Com isso um servidor local será iniciado. Acesse http://localhost:8000 para vizualisar o site e webservice.

=============
Interface web
=============

Um site simples foi criado para servir de interface para testar todos os desafios desenvolvidos.
Para acessar acesse o localhost http://127.0.0.1:8000

===========
Web Service
===========

O Web Service foi criado utilizando RESTful.
Códigos exemplos podem ser encontrados no arquivo Exemplos.txt

=================
Dúvidas e Contato
=================

joseloolo@hotmail.com
