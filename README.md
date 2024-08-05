# Django Test Assignment Boilerplate

A take on typical test assignments, this repository showcases a universal Django setup with sample features. Perfect for experimenting with Django's capabilities.

## Project Description

The API for this system includes endpoints for user registration, login, logout. Credentials are provided at the end of the file.

### Task Management System

Each task includes a title and a description. Users are required to register and log in to access task management functionalities. All tasks are accessible to all users.

### Advert Views Counter

Track and manage the number of views for each advert. The counter automatically increments each time an advert is accessed via its detail view, allowing you to monitor engagement and popularity effectively.

## API Endpoints

### auth

1. User Registration
    - `/api/auth/registration/` (POST)
        - Register a new user.

2. User Login
    - `/api/auth/login/` (POST)
        - Log in a user.

3. User Logout
    - `/api/auth/logout/` (POST)
        - Log out a user.

### task managment

4. Tasks List
    - `/api/tasks/` (GET)
        - Retrieve a list of all tasks. Only the task's ID and title are included in each task.
    - `/api/tasks/` (POST)
        - Create a new task. The request body should contain `title` and `description`.

5. Task Detail
    - `/api/tasks/{id}/` (GET)
        - Retrieve details of the task with the given ID. All fields of the task are included.
    - `/api/tasks/{id}/` (PUT)
        - Update the task with the given ID. The request body should contain `title` and `description`.
    - `/api/tasks/{id}/` (DELETE)
        - Delete the task with the given ID.

### advert views counter

6. Advert List
    - `/api/adverts/` (GET)
        - Retrieve a list of all adverts. Includes all fields of each advert plus the city name and category name.

7. Advert Detail
    - `/api/advert/{advert_pk}/` (GET)
        - Retrieve details of the advert with the given ID. Includes all fields of the advert. Accessing this endpoint increases the view count of the advert.


## Requirements

- Docker
- Docker Compose

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:

    ```shell
    git clone https://github.com/la-coderoque/task-management-system.git
    cd task-management-system
    ```

2. Build and start the Docker containers:

    ```shell
    docker compose build
    docker compose up
    ```

## API Documentation

This application uses Swagger UI for interactive API documentation and exploration. Once the application is running, the Swagger UI interface is accessible at [http://localhost:8080/](http://localhost:8080/).

From the Swagger UI interface, you can:

    View the entire API schema, including paths, operations, parameters, request bodies, and responses.
    Send requests and receive responses from the API.
    View clear error messages.
    Easily interact with the API without needing to use a separate tool like curl or Postman.

Note that in order to interact with endpoints that require authentication, you'll need to log in. The default superuser username and password are both admin.

## Admin Interface

### Superuser

By default, a superuser is created during the initialization process with the following credentials:

Username: admin
Password: admin

These can be customized by setting the environment variables `DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_PASSWORD` in the Docker compose file.

Django's admin interface is available at [http://localhost:8000/admin](http://localhost:8000/admin).
