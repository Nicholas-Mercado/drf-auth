# LAB - Class 33

Project: drf-auth

Author: Nicholas Mercado

## Links and Resources

[Django](https://www.djangoproject.com/)

[psycopg2-binary 2.9.3](https://pypi.org/project/psycopg2-binary/)

## Tests

How do you run tests?

python manage.py test

Any tests of note?

[Test found here](book/tests.py)

## Thunder Client

**Post**

http://localhost:8000/api/token/

In Body

{
    "username" :"admin",
    "password": "admin"
}

**Get**

http://localhost:8000/api/v1/book

In Auth add access key
