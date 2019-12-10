<h2>Instalar</h2>

Para instalar as depêndencias necessárias, execute:
```
pip install -r requisitos.txt
```
Ou instale manualmente os pacotes cujos nomes estão no arquivo requisitos.txt

<h2>Configurações</h2>

Após instalar as dependências e antes de executar o projeto, executar os seguintes comandos estando na pasta raiz do projeto.

Para configurações inicias
```
python manage.py makemigrations
```

Logo após executar para criar o banco de dados
```
python manage.py migrate
```

<h2>Executar</h2>

Para executar o projeto, executar o seguinte comando estando na pasta raiz do projeto.
```
python manage.py runserver
```

Com isso um servidor local será iniciado. Acesse http://localhost:8000 para vizualisar o site e webservice.

<h2>Interface web</h2>

Um site simples foi criado para servir de interface para testar todos os desafios desenvolvidos.
Para acessar acesse o localhost http://127.0.0.1:8000

<h2>Web Service</h2>

O Web Service foi criado utilizando RESTful.
Serão listados os Métodos HTTP de cada etapa do desafio juntamente com um código exemplo.

<h3>Resumo Criptográfico</h3>

<b>GET</b> - Retorna todos os resumos criados até o momento.
```
Codigo aqui
```
<b>POST</b> - Envia um arquivo para o servidor e retorna um json com o resumo criptografico.
```
Codigo aqui
```

<h3>Chaves Assimétricas</h3>

<b>GET</b> - Retorna todas as chaves assimétricas criadas até o momento.
```
Codigo aqui
```
<b>POST</b> - Envia um int >=1024 e retorna uma chave assimétrica contendo a quantidade de bits passada.
```
Codigo aqui
```

<h3>Certificado Raiz</h3>

<b>POST</b> - Apesas o método POST, sem nenhum argumento. Retorna um json avisando se criou ou não um certificado AC-RAIZ.
Os dados do certificado já estão definidos no código, por esse motivo não há argumentos.
```
Codigo aqui
```

<h3>Certificados Assinados pela AC-RAIZ</h3>

<b>GET</b> - Retorna uma lista com todos os certificados criados e assinados pela AC-RAIZ até o momento.
```
Codigo aqui
```
<b>POST</b> - Envia um número serial e informações para o servidor e cria um certificado assinado pela AC-RAIZ. O certificado fica armazenado no servidor.
```
Codigo aqui
```

<h2>Dúvidas e Contato</h2>

- [X] joseloolo@hotmail.com
- [X] (48) 99970-8959 (Wpp e Telegram)
