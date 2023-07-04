# Task Management System

This project is a simple task management system implemented with Django, Django Rest Framework, and MySQL. The system allows users to create, view, update, and delete tasks.

## Project Description

Each task includes a title and a description. Users are required to register and log in to access task management functionalities. All tasks are accessible to all users.

The API for this system includes endpoints for user registration, login, logout, retrieving a list of all tasks, creating a new task, retrieving details of a task, updating a task, and deleting a task.

## API Endpoints

1. User Registration
    - `/api/auth/registration/` (POST)
        - Register a new user.

2. User Login
    - `/api/auth/login/` (POST)
        - Log in a user.

3. User Logout
    - `/api/auth/logout/` (POST)
        - Log out a user.

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
    docker-compose build
    docker-compose up
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
