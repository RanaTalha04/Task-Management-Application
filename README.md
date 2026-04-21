# Task Management Application

A backend-only task management application built with FastAPI and Python.

## Description

This application provides a RESTful API for managing tasks. Users can create, read, update, and delete tasks. 
<!-- It includes features like user authentication, task categorization, and priority levels. -->

## Features

- User registration <!-- and authentication -->
- Create, read, update, and delete tasks
- API documentation with Swagger UI
<!-- - Task categorization and priority assignment
- Due date management -->

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.13+
- **Database**: PostgreSQL 
- **Dependencies**: Managed with pip
<!-- - **Authentication**: JWT tokens -->

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd task-management-app
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables (create a `.env` file):
   ```
   DATABASE_URL= "postgresql+psycopg://username:password@host_name:port_number/tasks.db"
   ```

4. Run the application:
   ```
   fastapi dev main.py --reload
   ```

## Usage

- Access the API at `http://localhost:8000`
- API documentation available at `http://localhost:8000/docs`
- You can use POSTMAN for API checking.

<!-- ### Example API Endpoints

- `POST /auth/login` - Login and get JWT token -->
- `POST /user/register` - Register a new user
- `GET /tasks/fetch` - Get all tasks
- `GET /tasks/one_task/{task_id}` - Get one task
- `POST /tasks/create` - Create a new task
- `PUT /tasks/update/{task_id}` - Update a task
- `DELETE /tasks/delete/{task_id}` - Delete a task 

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Author 

Muhammad Talha