# ACM Education Platform - Backend Documentation

## Table of Contents
1. [Overview](#overview)
2. [Technology Stack](#technology-stack)
3. [Project Structure](#project-structure)
4. [Environment Setup](#environment-setup)
5. [Database Configuration](#database-configuration)
6. [API Endpoints](#api-endpoints)
7. [Authentication](#authentication)
8. [AI Integration](#ai-integration)
9. [Deployment](#deployment)
10. [Troubleshooting](#troubleshooting)
11. [Future Development](#future-development)

## Overview

The ACM Education Platform is a Flask-based web application designed to manage educational resources, including courses, exams, and AI-powered student assessments. The platform allows teachers to create and manage courses and exams, while students can enroll in courses, take exams, and receive AI-generated feedback on their performance.

### Key Features
- User management (students and teachers)
- Course management
- Exam creation and administration
- AI-powered evaluation of student answers
- RESTful API for frontend integration

## Technology Stack

The backend of the ACM Education Platform is built using the following technologies:

- **Python 3.x**: The primary programming language
- **Flask**: Web framework for building the API
- **SQLAlchemy**: ORM for database interactions
- **MySQL/PostgreSQL**: Database options (configurable)
- **LangChain**: Framework for AI-powered features
- **Python-dotenv**: For environment variable management

## Project Structure

The backend follows a modular structure organized by functionality:

```
project_root/
├── run.py                  # Application entry point
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in version control)
├── app/                    # Main application package
│   ├── __init__.py         # Application factory and initialization
│   ├── config.py           # Configuration settings
│   ├── database.py         # Database configuration
│   ├── models/             # Database models
│   │   ├── __init__.py
│   │   ├── student_model.py
│   │   ├── teacher_model.py
│   │   ├── course_model.py
│   │   ├── exam_model.py
│   │   ├── question_model.py
│   │   ├── answer_model.py
│   │   ├── studentAnswer_model.py
│   │   ├── enrollment_model.py
│   │   └── ai_assessment_model.py
│   ├── routes/             # API endpoints
│   │   ├── __init__.py
│   │   ├── main_routes.py
│   │   ├── user_routes.py
│   │   ├── student_routes.py
│   │   ├── teacher_routes.py
│   │   ├── course_routes.py
│   │   ├── exam_routes.py
│   │   ├── question_routes.py
│   │   ├── answer_routes.py
│   │   ├── studentAnswer_routes.py
│   │   ├── enrollment_routes.py
│   │   └── ai_assessment_routes.py
│   ├── services/           # Business logic
│   ├── repositories/       # Data access layer
│   ├── utils/              # Utility functions
│   ├── webhooks/           # Webhook handlers
│   ├── langchain/          # AI integration
│   │   ├── __init__.py
│   │   ├── chains.py
│   │   └── prompts.py
│   └── doc/                # Documentation
│       ├── SETUP.md
│       ├── STRUCTURE.md
│       ├── ENDPOINTS.md
│       └── Schema.sql
```

## Environment Setup

### Prerequisites
- Python 3.8 or higher
- MySQL or PostgreSQL database
- Git

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:
   ```
   # MySQL credentials
   MYSQL_HOST=127.0.0.1:3306
   MYSQL_USER=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DB=acm_education
   
   # Secret key for Flask sessions
   SECRET_KEY=your_secret_key
   
   # PostgreSQL credentials (if using PostgreSQL instead of MySQL)
   PGHOST=your_pg_host
   PGDATABASE=your_pg_database
   PGUSER=your_pg_username
   PGPASSWORD=your_pg_password
   ```

5. Run the application:
   ```bash
   python run.py
   ```

The application will be available at `http://localhost:5000`.

## Database Configuration

The application supports both MySQL and PostgreSQL databases. The default configuration uses MySQL, but you can switch to PostgreSQL by modifying the `config.py` file.

### MySQL Configuration
MySQL is configured by default in the `config.py` file. Ensure you have the following environment variables set in your `.env` file:
```
MYSQL_HOST=127.0.0.1:3306
MYSQL_USER=your_mysql_username
MYSQL_PASSWORD=your_mysql_password
MYSQL_DB=acm_education
```

### PostgreSQL Configuration
To use PostgreSQL instead of MySQL, you need to:

1. Uncomment the PostgreSQL configuration section in `app/config.py`
2. Comment out the MySQL configuration section
3. Ensure you have the following environment variables set in your `.env` file:
```
PGHOST=your_pg_host
PGDATABASE=your_pg_database
PGUSER=your_pg_username
PGPASSWORD=your_pg_password
```

### Database Schema
The database schema is defined in `app/doc/Schema.sql`. This file contains the SQL statements to create all the necessary tables for both MySQL and PostgreSQL.

Key tables in the database:
- `Student`: Stores student information
- `Teacher`: Stores teacher information
- `Course`: Stores course information
- `Enrollment`: Manages student enrollment in courses
- `Exam`: Stores exam information
- `Question`: Stores exam questions
- `Answer`: Stores correct answers to questions
- `Student_Answer`: Stores student responses to questions
- `AI_Assessment`: Stores AI-generated assessments of student answers

## API Endpoints

The application provides a RESTful API with the following main endpoint categories:

1. **User Management**
   - Student registration and management
   - Teacher registration and management

2. **Course Management**
   - Create, read, update, and delete courses
   - Manage course enrollment

3. **Exam Management**
   - Create, read, update, and delete exams
   - Manage exam questions and answers

4. **Student Answers**
   - Submit and retrieve student answers
   - Get AI assessments for student answers

For a complete list of API endpoints with request/response examples, refer to `app/doc/ENDPOINTS.md`.

## Authentication

The application uses Clerk for authentication. When a user logs in through the frontend, Clerk provides a token that is used to authenticate API requests.

### User Types
- **Students**: Can enroll in courses, take exams, and view their assessments
- **Teachers**: Can create and manage courses, exams, and view student assessments
- **Admins**: Have all teacher permissions plus additional administrative capabilities

## AI Integration

The application uses LangChain for AI-powered features, particularly for assessing student answers. The AI integration is implemented in the `app/langchain` directory.

### Key Components
- `chains.py`: Contains LangChain chain implementations
- `prompts.py`: Contains prompt templates for the language model

### AI Assessment Process
1. A student submits an answer to a question
2. The answer is sent to the AI assessment service
3. The AI generates an assessment and grade based on the answer and the correct answer
4. The assessment is stored in the database and returned to the student

## Deployment

### Development Environment
For development, run the application using:
```bash
python run.py
```

### Production Environment
For production deployment, consider the following:

1. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 "app:create_app()"
   ```

2. Set up a reverse proxy with Nginx or Apache

3. Configure environment variables for production:
   - Set `DEBUG=False`
   - Use a strong, random `SECRET_KEY`
   - Configure database connection pooling

4. Set up monitoring and logging

## Troubleshooting

### Common Issues

1. **Database Connection Errors**
   - Verify database credentials in `.env` file
   - Ensure the database server is running
   - Check network connectivity to the database server

2. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check for circular imports in the codebase

3. **Authentication Issues**
   - Verify Clerk configuration
   - Check that the frontend is sending the correct authentication headers

### Debugging

The application runs in debug mode by default in development, which provides detailed error messages. To enable more verbose logging, modify the logging configuration in `app/__init__.py`.

## Future Development

Areas for future improvement:

1. **Enhanced AI Features**
   - Implement more sophisticated assessment algorithms
   - Add personalized learning recommendations

2. **Performance Optimization**
   - Implement caching for frequently accessed data
   - Optimize database queries

3. **Additional Features**
   - Real-time notifications
   - Advanced analytics for teachers
   - Integration with learning management systems

4. **Testing**
   - Expand unit test coverage
   - Add integration tests
   - Implement automated testing in CI/CD pipeline

---

This documentation is maintained by the ACM Education Platform team. For questions or support, please contact [contact information].

Last updated: [3/10/25] 