## Sobre o projeto
Uma API-rest desenvolvida com a finalidade de armazenar dados de arquivos CNAB. Esses arquivos são tratados no <a href="https://github.com/byetevinn/cnab-conversion-front">Front-End</a> e inseridos em um banco de dados com essa API.

## Como instalar e rodar a aplicação

1- Clone o repositório em sua máquina

2- Crie um ambiente virtual usando o comando `python -m venv venv`

3- Inicie o ambiente virtual com o comando `source venv/bin/activate`

4- Instale todas as dependências necessárias usando o comando `pip install -r requirements.txt`

5- Crie as suas variáveis de ambiente usando o exemplo do `.env-example`

6- Para criar as tabelas no banco de dados use o comando `python manage.py migrate`

7- Por fim use o comando `python manage.py runserver` para rodar a aplicação

## Deploy

- <a href="https://cnab-conversion-production.up.railway.app/">Deploy</a>

## Documentação

- <a href="https://cnab-conversion-production.up.railway.app/docs/swagger/">Swagger</a>
- <a href="https://cnab-conversion-production.up.railway.app/docs/redoc/">Redoc</a>

## Tecnologias usadas no projeto

#### Linguagem

- PYTHON

#### Framework

- DJANGO

#### Banco de dados

- POSTGRESQL

#### Bibliotecas

- DJANGO-REST-FRAMEWORK
- DJANGO-CORS-HEADERS
- PSYCOPG2-BINARY
- PYTHON-DOTENV
- DRF-SPECTACULAR
