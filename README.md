# django-auth

## Prerequisites

- Python 3.5>
- POSTMAN
- Virtualenv
- Git

## Instalation

    $ virtualenv python=python3 venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ python manage.py migrate
    $ python manage.py createsuperuser


## Run project

    $ python manage.py runserver


## API

### Users

#### Create users
> **POST** /api/v1/accounts/register/

- **username**
- **password**
- **password_confirm**
- **email**
- **first_name**
- **last_name**

##### Response

**HTTP/1.1 201 OK**
- **id**
- **username**
- **email**
- **first_name**
- **last_name**


#### List users

> **GET** /api/v1/users/
##### Response

**HTTP/1.1 200 OK**

List of users registered

### Tokens
#### Access

> **POST** /api/v1/token/access/

- **email**
- **password**

##### Response

**HTTP/1.1 200 OK**

- **access**
- **refresh**

#### Refresh

> **POST** /api/v1/token/refresh/
- **access**
- **refresh**

##### Response

**HTTP/1.1 201 OK**

- **access**
- **refresh**
