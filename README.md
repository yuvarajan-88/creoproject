# creoproject

Creoproject is a Django-based web application for managing student information and their subject marks. The project allows you to add, view, and manage student details along with their marks in various subjects.

## Features

- Add student details (Name, Age, Email, City, and Image)
- Add marks for students in various subjects (Language 1, Language 2, Acting, Dance)
- View student details and their subject marks on a single page
- Simple and user-friendly interface

## Installation
open command prompt
i)python - from website
  verification - python --version
ii)Django - pip install django
  verification - django-admin --version


Prerequisites:
- Python 3.11.9
- Django 5.0.6


### creating environment , project and app
i)virtual enviroment -py -m venv myworld,myworld\Scripts\activate.bat
ii)creating folder name -md creoproject
open vs code
iii)install django - py -m pip install Django
iv)project - python manage.py startproject yuvarajproject
v)App - py manage.py startapp yuvarajapp


Project Directory (yuvarajproject):
writing neccesary code in setting and url.py

App Directory (yuvarajapp):
writing neccesary code in model,views,urls,settings.py

#### Templates:
creating html files namely studetails.html and home.html.

File structure:
creoproject/
├── yuvarajproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── yuvarajapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   │   ├── __init__.py
│   ├── templates/
│   │   ├── home.html
│   │   ├── studetails.html
├── manage.py
├── db.sqlite3

###### Apply mitigation:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver

####### Access the application:
Open your web browser and go to http://127.0.0.1:8000/.

Usage:

Adding Student Details:
Navigate to the Django admin interface at http://127.0.0.1:8000/admin/.
Log in with your admin credentials.
Add new students by filling in their details (Name, Age, Email, City, and Image).


Viewing Student Details:
Go to http://127.0.0.1:8000/student/id/, where id is the student's ID.
View the student's details and their subject marks on the page.








