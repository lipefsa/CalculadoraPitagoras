# <p align="center"> Calculadora de Pitágoras </p>

<p align="center"> Esta é uma aplicação simples que permite que o usuário calcule a hipotenusa de um triângulo retângulo usando o Teorema de Pitágoras.</p>

## :computer: Requisitos:

<ul>
     <li><a href="https://www.python.org/downloads/">Python 3</a></li>
     <li><a href="https://flask.palletsprojects.com/en/2.2.x/installation/">Flask</a></li>
      <li><a href="https://flask-cors.readthedocs.io/en/latest/">Flask-Cors</a></li>
</ul>

## :fire: Instalação:



1. Clone o repositório: `git clone https://github.com/lipefsa/calculadora-pitagoras`

2. Mude para a pasta do projeto: `cd calculadora-pitagoras`

3. Crie um ambiente virtual: `python3 -m venv venv`

4. Ative o ambiente virtual: `source venv/bin/activate`

5. Instale as dependências: `pip install -r requirements.txt`


## :dart: Executando o App



1. Inicie o server: `python main.py`

2. Abra seu navegador e vá para o endereço `http://localhost:5000`

3. Coloque os valores dos dois lados do triângulo e use o botão de Calcular

4. O resultado será exibido na página.


## :mag: Testando


Para testar o aplicativo envie uma requisição GET para o endpoint.
Por exemplo:

```
$ curl http://localhost:5000/api?a=3&b=4
```


<p align="center">Feito por <strong><a href="https://www.linkedin.com/in/phelipe-macel">Phelipe Macel</a> 💻 </strong></p>