# Singular's Project manager

Prototype for Singular`s coding exercise.

Simple SPA that allows the user inspect their clients and their respective projects database in an organized and scalable fashon.

Full original requirements: _./Coding Assignment_D.pdf_. 

## Features
- Latest python3 runtime environment.
- Backend powered with Django 2
- SQLite3 relational database
- Frontend powered with Vue.js
- CI Deployement on Heroku


## How to Use

To use this project, follow these steps:

1. Create your Python 3.6 runtime environment.
2. Install python dependencies: `$ pip install -r requirements.txt` 
3. Run database migrations: `$ python manage.py migrate`
4. Run django backend server: `$ python manage.py runserver 8000` 


## Note

For the sake of quicker prototyping, Vue.js has been added through CDN.

For further scaling, its advised to completely separate frontend from backend, and to establish communication between
them through an API. 
