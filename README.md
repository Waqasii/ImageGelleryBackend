# Image Gallery App Backend

## Introduction

This is a Django app that uses GraphQL with JWT authentication and a PostgreSQL database. The app is designed to provide an image gallery functionality with features like upload, Delete and List images. The app (Backend) implemented using the Django framework and Graphene-Django for GraphQL.

## Installation

To install the dependencies, you can use pip to install from the requirements file. Run the following command in your terminal:

`pip install -r requirements.txt`


## Database Configuration

The app uses a PostgreSQL database. To configure the database, update the following settings in your Django project's `settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ImageGallery',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Make sure to replace the NAME, USER, PASSWORD, HOST, and PORT values with your own database settings.


## Running the App
To run the app, navigate to the project directory in your terminal and run the following command:

`python manage.py runserver`

This will start the development server at http://localhost:8000/

 ## GraphQL Endpoint
The GraphQL endpoint for the app is located at http://localhost:8000/graphql/. You can access the GraphQL IDE by visiting http://localhost:8000/graphql/ in your web browser.

