# recipe-app-api

## List of commands for Docker Python App

### Build the project

`docker-compose build`

### Run the app

`docker-compose up`

### Stop the app

`docker-compose down`

### Adding new app

`docker-compose run --rm app sh -c "python manage.py startapp user"`

### Run all test cases

`docker-compose run --rm app sh -c "python manage.py test"`

### Make migration when you have updated entity or added new entity

`docker-compose run --rm app sh -c "python manage.py makemigrations"`

### Create super user in docker database

`docker-compose run --rm app sh -c "python manage.py createsuperuser"`
