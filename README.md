# Mini e-commerce
O link da API é https://mini-ecommerce-bemol.herokuapp.com

## Tecnologias usadas
- Python
- Django
- Django rest framework
- CI/CD

## Bibliotecas usadas
- Faker (mock dos testes)
- SQLite3 (banco de dados local e para testes)
- PotsgreSQL (banco de dados na nuvem(heroku))
- gunicorn (deploy)
- python-dotenv (SECRET_KEY no arquivo .env)
- django-cors-headers (Pra resolver problemas relacionados ao CORS)

## Usando localmente
Para usar a api localmente basta digitar os seguintes comandos no terminal
- python -m venv venv
- source venv/bin/activate
- pip install --upgrade pip
- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## Endpoints da api
### /api/users/register/
Rota responsável pela criação de usuários

Métodos permitidos: POST

Corpo da requisição:


```
{
 ​"email​": ​string​,
 ​"password​": ​string​,
 ​"name​": ​string​,
 ​"address​": ​{
   ​"cep​": ​string​,
   ​"number​": ​string​,
   ​"bairro​": ​string​,
   ​"cidade​": ​string​,
   ​"rua​": ​string​,
   ​"uf​": ​string​,
 ​}​,
}​;
```
### /api/users/login/
Rota responsável pelo login de usuários

Métodos permitidos:POST

Corpo da requisição:

```
{
    "email​": ​string​,
    "password​": ​string​,
}
```
