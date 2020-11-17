# Petgram Django REST API

This a Django 3.0+ project for Software House Mérida Development Challenge.

## Features

- Django 3.0+
- Uses [Virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) - Tool to create isolated Python environments.
- [Django REST Framework](https://www.django-rest-framework.org/) - Powerful and flexible toolkit for building Web APIs.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - The Amazon Web Services (AWS) SDK for Python.
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) - A JSON Web Token authentication plugin for the Django REST Framework.
- Procfile for running gunicorn with New Relic's Python agent.
- PostgreSQL database support with psycopg2.

## Prerequisites

- Python 3.5>
- Virtualenv

## How to install

```bash
$ virtualenv python=python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Environment variables

These settings are used on development and production environments.

```
DJANGO_SECRET_KEY=your-django-secret-key
DJANGO_ALLOWED_HOSTS='localhost 0.0.0.0 127.0.0.1 [::1]'
DJANGO_ALLOWED_ORIGINS='http://localhost:3000'
DJANGO_DEBUG=1
ADMIN_ENABLED=1
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name
DATABASE_URL=postgres://postgres:s3cr3t@localhost:5432/mydb
```

See `.env.example`

## Deployment

### Database setup

```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```

### Run project

    $ python manage.py runserver

## API

### Users

#### Create users

> **POST** /api/v1/accounts/register/

- **username**
- **email**
- **fullname**
- **password**
- **password_confirm**

##### Response

**HTTP/1.1 201 OK**

- **id**
- **username**
- **email**
- **fullname**

#### List users

> **GET** /api/v1/users/

##### Response

**HTTP/1.1 200 OK**

List of users registered

### Tokens

#### Access

> **POST** /api/v1/token/access/

- **username**
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

See the complete API reference [here](https://documenter.getpostman.com/view/4606205/TVeqc6kn) or use the DRF Browseable API available in https://petgram-demo.herokuapp.com/api/v1/


## License

The MIT License (MIT)

Copyright (c) 2020 Raúl Novelo

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
