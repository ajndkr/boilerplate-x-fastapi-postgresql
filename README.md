# FastAPI Chat Application

This is a full stack chat application built with FastAPI and PostgreSQL. The application provides a single `/chat` endpoint for users to communicate with each other in real-time.

## Installation

1. Clone the repository
2. Install the required dependencies with `pip install -r requirements.txt`
3. Start the application with `uvicorn app.main:app --reload`

## Usage

Once the application is running, navigate to `http://localhost:8000/docs` to access the Swagger UI and interact with the `/chat` endpoint.

## Project Structure

The project follows the following structure:

- `app/`: Contains the main application code
  - `main.py`: Entry point for the application
  - `database.py`: Database configuration and connection
  - `models.py`: Database models
  - `schemas.py`: Pydantic schemas for request and response objects
  - `routers/`: Contains the router for the `/chat` endpoint
    - `__init__.py`: Initializes the router
    - `chat.py`: Contains the `/chat` endpoint logic
- `tests/`: Contains the unit tests for the application
  - `test_main.py`: Tests for the main application code
  - `test_database.py`: Tests for the database configuration and connection
  - `test_models.py`: Tests for the database models
  - `test_schemas.py`: Tests for the Pydantic schemas
  - `test_routers/`: Contains the tests for the `/chat` endpoint
    - `__init__.py`: Initializes the tests
    - `test_chat.py`: Tests for the `/chat` endpoint logic
- `alembic/`: Contains the database migration scripts
  - `alembic.ini`: Alembic configuration file
  - `versions/`: Contains the migration scripts
    - `__init__.py`: Initializes the migration scripts
    - `initial.py`: Initial migration script
- `docker-compose.yml`: Docker Compose configuration file for running the application and database in containers
- `Dockerfile`: Dockerfile for building the application image
- `.github/`: Contains the GitHub Actions workflow for continuous integration
  - `.github/workflows/python-app.yml`: Workflow for running the unit tests on push and pull request events
- `.pre-commit-config.yaml`: Configuration file for pre-commit hooks.