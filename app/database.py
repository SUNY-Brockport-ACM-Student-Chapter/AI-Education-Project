"""
database.py

This module sets up the connection to the database using SQLAlchemy.
It configures the database engine, creates a session factory for handling
database transactions, and defines a base class for all database models.

Dependencies:
- SQLAlchemy
- sessionmaker
- declarative_base

Functions:
- init_db(app): Initializes the database and creates a session for the given app.
- get_db_session(): Returns a new database session.

Usage:
- Call `init_db(app)` during application startup to set up the database.
- Use `get_db_session()` to obtain a session for database operations.
"""

import enum

from sqlalchemy import Enum, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import SQLALCHEMY_DATABASE_URI

# Create base class for declarative models
Base = declarative_base()

# Database URL configuration
SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URI

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create SessionLocal class
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(app):
    """
    Initializes the database and creates a session for the given app.

    Args:
        app: The application instance to attach the session to.
    """
    Base.metadata.create_all(engine)  # Use the existing engine
    app.session = session_local()  # Use the existing SessionLocal


def get_db_session():
    """
    Returns a new database session.

    Returns:
        A new session object for database operations.
    """
    return session_local()


# Define the enum classes
class RoleEnum(enum.Enum):
    """Enumeration defining possible user roles in the system."""
    ADMIN = "admin"
    TEACHER = "teacher"


class EnrollmentStatusEnum(enum.Enum):
    """Enumeration defining possible states for course enrollment."""
    ENROLLED = "enrolled"
    CANCELLED = "cancelled"
    PENDING = "pending"


role_enum = Enum(RoleEnum, name="role_enum")
enrollment_status_enum = Enum(EnrollmentStatusEnum, name="enrollment_status_enum")
