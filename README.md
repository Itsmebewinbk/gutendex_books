

This is an application build using Python Django and Django REST framework.

## Cloning the Repository and moving to the project level

```sh
git clone https://github.com/Itsmebewinbk/gutendex_books.git
cd gutendex_books

```

## Installation and Setup

The application requires [Python](https://www.python.org/) v3.6+ to run.


Install the dependencies and requirements after creating a virtual environment for the project.

```sh
python3 -m venv env
pip install -r requirements.txt
```
```sh
    
    mkdir logs  (create logs directory)
    nano .env  (add SECRET_KEY and ENVIRONMENT)
```
if environment is dev then create psql_db and include  [DB_NAME,DB_USER,DB_PASSWORD,DB_HOST] in .env file


Initializing the project
```sh
python manage.py migrate
```

Admin user creation (optional) for accessing the django admin
```sh
python manage.py createsuperuser
```

## Running the project

To start the Django development server
```sh
python manage.py runserver
```


##### Home:
A basic index page
```sh
http://localhost:8000
```
##### Admin:
The Django admin UI
```sh
http://localhost:8000/api/admin/
```
##### API Documentation:
API Documentation page done using [Swagger](https://drf-yasg.readthedocs.io/en/stable/readme.html)
```sh
http://localhost:8000/api/docs/
```

Once this is done the Application is good to go.
