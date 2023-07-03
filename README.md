# Task Management System

This project is a simple task management system implemented with Django, Django Rest Framework, and MySQL. The system allows users to create, view, update, and delete tasks.

## Project Description

Each task includes a title and a description. Users are required to register and log in to access task management functionalities. All tasks are accessible to all users.

The API for this system includes endpoints for user registration, login, logout, retrieving user details, retrieving a list of all tasks, creating a new task, retrieving details of a task, updating a task, and deleting a task.

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

4. Get User Details
    - `/api/auth/user/` (GET)
        - Get details of the current user.

5. Tasks List
    - `/api/tasks/` (GET)
        - Retrieve a list of all tasks. Only the task's ID and title are included in each task.
    - `/api/tasks/` (POST)
        - Create a new task. The request body should contain `title` and `description`.

6. Task Detail
    - `/api/tasks/{id}/` (GET)
        - Retrieve details of the task with the given ID. All fields of the task are included.
    - `/api/tasks/{id}/` (PUT)
        - Update the task with the given ID. The request body should contain `title` and `description`.
    - `/api/tasks/{id}/` (DELETE)
        - Delete the task with the given ID.

## Installation and Usage
