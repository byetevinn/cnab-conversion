## Sobre o projeto
Uma API-rest desenvolvida com a finalidade de armazenar dados de arquivos CNAB. Esses arquivos são tratados no <a href="https://github.com/byetevinn/cnab-conversion-front">Front-End</a> e inseridos em um banco de dados com essa API.

## Como instalar e rodar a aplicação

1- Crie seu database no postgreSQL

2- Clone o repositório em sua máquina

3- Crie um ambiente virtual usando o comando `python -m venv venv`

4- Inicie o ambiente virtual com o comando `source venv/bin/activate`

5- Instale todas as dependências necessárias usando o comando `pip install -r requirements.txt`

6- Crie as suas variáveis de ambiente usando o exemplo do `.env-example`

7- Para criar as tabelas no banco de dados use o comando `python manage.py migrate`

8- Por fim use o comando `python manage.py runserver` para rodar a aplicação

## Documentação

- Swagger: Acrescente `/docs/swagger/` na sua URL
- Redoc: Acrescente `/docs/redoc/` na sua URL

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
