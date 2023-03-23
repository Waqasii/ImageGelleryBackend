# Image Gallery App Backend

## Introduction

This is a Django app that uses GraphQL with JWT authentication and a PostgreSQL database. The app is designed to provide an image gallery functionality with features like upload, Delete and List images. The app (Backend) implemented using the Django framework and Graphene-Django for GraphQL.

## Installation

To install the dependencies, you can use pip to install from the requirements file. Run the following command in your terminal:

`pip install -r requirements.txt`

## CreateSuperUser for Login

Follow these steps to create a superuser and use the same user for login on the frontend:
1. Open the terminal or command prompt and navigate to the root directory of your Django project.
2. Run the following command to create a superuser:
    `python manage.py createsuperuser`
3. Enter the required details when prompted (username, email, password, etc.).
4. Once the superuser is created successfully, navigate to your React app's login page in the frontend.
5. Enter the superuser's credentials (username and password) to log in.

That's it! You should now be able to log in to the frontend using the superuser account you created.

## Database Configuration

The app uses a PostgreSQL database. To configure the database, you will have to create the DB by using pgAdmin and then update the following settings in your Django project's `settings.py` file:

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

