# SIMPLE REST API EXAMPLE - Python - DJANGO - Django Rest Framework
This is a sample of how make a simple rest-api with Python, Django and django-rest-framework
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Requirements
- Python 3.6
- Django (2.2.1)
- Django REST Framework

## Installation
```
	pip install django
	pip install djangorestframework

```

## Structure
A RESTfull API's, are definide by endpoints. This structure allow end users and applications, access data from our application using the HTTP methods - GET, POST, PUT, DELETE.

We have one single resource, `employee`, so we will use the following URLS - `/employee/` and `/employee/<id>` for detailed element, or specific method, respectively:

The resource can list, add, update and remove employees

Endpoint |HTTP Method | Result
---------|----|-------
`employee` | GET | Get a list of all employees
`employee/:id` | GET | Get a single employee
`employee`| POST | Insert a new employee
`employee/:id` | PUT | Update a employee
`employee/:id` | DELETE | Delete a employee

## Using the API
We can test the API using [curl](https://curl.haxx.se/) or [httpie](https://github.com/jakubroztocil/httpie#installation). Httpie is a user friendly http client that's written in Python.

You can install httpie using pip:
```
pip install httpie
```
First, we have to start up Django's development server.
```
	python manage.py runserver

```

Calling the below endpoints from another terminal

Endpoint |HTTP Method | Result
---------|----|-------
`employee` | GET | Get a list of all employees
```
	http http://127.0.0.1:8000/employee/
```
we list all employees

    {
        "name": "Thales G",
        "email": "thales@test.com",
        "department": "Engenharia"
    },
    {
        "name": "Kleber Alves",
        "email": "kleber_alves_rock@test.com",
        "department": "Laboratório de Ciência de dados"
    },
    {
        "name": "Thiago Bueno",
        "email": "thiago.msbueno@gmail.com",
        "department": "Engenharia"
    },
    {
        "name": "Ariane C",
        "email": "ariane@test.com",
        "department": "Hospotal das Clinicas"
    },
    {
        "name": "Leonardo",
        "email": "leomsbueno@hotmail.com",
        "department": "UFSCAR"
    }


Endpoint |HTTP Method | Result
---------|----|-------
`employee/:id` | GET | Get a single employee

```
	http http://127.0.0.1:8000/employee/4
```
We get the employee with id = 4
```
{
    "name": "Kleber Alves",
    "email": "kleber_alves_rock@test.com",
    "department": "Laboratório de Ciência de dados"
}
```
Endpoint |HTTP Method | Result
---------|----|-------
`employee`| POST | Insert a new employee

```
http --json -v POST localhost:8000/employee/ name=John email=john@example.org department=helthcare
```
We can insert a new employee in our API with post method

See the return below

```
HTTP/1.1 201 Created
Allow: GET, POST, OPTIONS
Content-Length: 67
Content-Type: application/json
Date: Wed, 05 Jun 2019 12:58:28 GMT
Server: WSGIServer/0.2 CPython/3.5.3
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "department": "helthcare",
    "email": "john@example.org",
    "name": "John"
}

```
Endpoint |HTTP Method | Result
---------|----|-------
`employee`| PUT | Update a existing employee

```
http --json -v PUT localhost:8000/employee/5 name=Carlos email=carlos@example.org department=Finance
```
We can update a new employee in our API with PUT method

See the return below

```
HTTP/1.1 200 OK
Allow: PUT, GET, DELETE, OPTIONS
Content-Length: 69
Content-Type: application/json
Date: Wed, 05 Jun 2019 13:05:36 GMT
Server: WSGIServer/0.2 CPython/3.5.3
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "department": "Finance",
    "email": "carlos@example.org",
    "name": "Carlos"
}
```

Endpoint |HTTP Method | Result
---------|----|-------
`employee`| DELETE | Delete a existing employee

```
	http --json -v DELETE localhost:8000/employee/5
```
We can update a new employee in our API with PUT method

See the return below

```
HTTP/1.1 204 No Content
Allow: PUT, GET, DELETE, OPTIONS
Content-Length: 0
Date: Wed, 05 Jun 2019 13:14:47 GMT
Server: WSGIServer/0.2 CPython/3.5.3
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

```
