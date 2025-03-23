# FastAPI Users API

## Overview
This is a simple FastAPI-based user management API that allows inserting and retrieving users from a database. The API provides a single endpoint `/users/` with a query parameter to specify the operation (Insert or Get).

## Features
- Insert a new user into the database
- Retrieve all users from the database
- Uses SQLAlchemy for database interactions

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn sqlalchemy
   ```
3. Set up the database by defining the required models in `models.py` and configuring the database connection in `database.py`.

## Running the Application
Start the FastAPI server using Uvicorn:
```sh
uvicorn main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

## API Endpoints
### 1. Insert a User
**Endpoint:**
```http
POST /users/
```
**Query Parameters:**
- `input=I` (for inserting a new user)
- `name`: User's name (required)
- `email`: User's email (required)
- `password`: User's password (required)

**Example Request:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/users/?input=I&name=JohnDoe&email=john@example.com&password=secret' \
     -H 'accept: application/json'
```

**Response:**
```json
{
  "CODE": "200",
  "MESSAGE": "User created successfully",
  "id": 1,
  "name": "JohnDoe",
  "email": "john@example.com"
}
```

### 2. Retrieve All Users
**Endpoint:**
```http
POST /users/
```
**Query Parameters:**
- `input=G` (for getting all users)

**Example Request:**
```sh
curl -X 'POST' 'http://127.0.0.1:8000/users/?input=G' \
     -H 'accept: application/json'
```

**Response:**
```json
{
  "CODE": "200",
  "MESSAGE": "User fetched successfully",
  "users": [
    {
      "id": 1,
      "name": "JohnDoe",
      "email": "john@example.com"
    }
  ]
}
```

## Project Structure
```
project-folder/
│── main.py           # FastAPI application
│── models.py         # SQLAlchemy models
│── database.py       # Database connection
│── routers/
│   └── users.py      # User API router
│── README.md         # Documentation
```

## Notes
- Ensure that `models.User` is properly defined in `models.py`.
- The database session is managed using dependency injection (`Depends(get_db)`).
- Error handling is implemented for invalid input flags.

## Author
Maintained by Rohit Kumar.

