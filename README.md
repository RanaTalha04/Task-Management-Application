# Task Management Application

A backend-only task management application built with FastAPI and Python.

## Description

This application provides a RESTful API for managing tasks. Users can create, read, update, and delete tasks. 
<!-- It includes features like user authentication, task categorization, and priority levels. -->

## Features

<!-- - User registration and authentication -->
- Create, read, update, and delete tasks
<!-- - Task categorization and priority assignment
- Due date management
- API documentation with Swagger UI -->

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.13+
- **Database**: PostgreSQL 
<!-- - **Authentication**: JWT tokens -->
- **Dependencies**: Managed with pip

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

- `POST /auth/register` - Register a new user
- `POST /auth/login` - Login and get JWT token
- `GET /tasks` - Get all tasks (authenticated)
- `POST /tasks` - Create a new task
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task -->

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Author 

Muhammad Talha