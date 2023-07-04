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

API documentation is available at [http://localhost:8080/](http://localhost:8080/).

## Admin Interface

# Superuser

By default, a superuser is created during the initialization process with the following credentials:

Username: admin
Password: admin

These can be customized by setting the environment variables `DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_PASSWORD` in the Docker compose file.

Django's admin interface is available at [http://localhost:8000/admin](http://localhost:8000/admin).
