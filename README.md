# SIMPLE REST API EXAMPLE - Python - DJANGO - Django Rest Framework
This is a sample of how make a simple rest-api with Python, Django and django-rest-framework.

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
`employee` | GET | Get a list of all emplyees
`employee/:id` | GET | Get a single employee
`employee`| POST | Insert a new employee
`employee/:id` | PUT | Update a emplyee
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

And than, we can call the endpoint and test the API from another terminal

```
	http http://127.0.0.1:8000/employee/
```
we get all emplyees

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



Try a call to endpoint employee with id 4:
```
	http http://127.0.0.1:8000/employee/4
```
we get the employee with id = 4
```
{
    "name": "Kleber Alves",
    "email": "kleber_alves_rock@test.com",
    "department": "Laboratório de Ciência de dados"
}
```
