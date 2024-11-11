"""
database.py

This module sets up the connection to the database using SQLAlchemy.
It configures the database engine, creates a session factory for handling
database transactions, and defines a base class for all database models.

The `get_db` function is used to provide a session for each request and 
ensure the session is closed after the request is processed.

Dependencies:
- SQLAlchemy
- sessionmaker
- declarative_base
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Move database URL to config file or environment variable
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Add echo=True during development for SQL logging
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=os.getenv("FLASK_ENV") == "development",
)

# Add some common configuration options
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,  # Useful for API responses
)

# Create a base class for the models to inherit
Base = declarative_base()


# Dependency for database session
def get_db():
    """
    Provide a new database session for each request.

    This function is a generator that yields a database session and ensures
    the session is properly closed after the request is processed. It is
    typically used as a dependency in FastAPI routes to handle database
    transactions.

    Yields:
        db (Session): A SQLAlchemy session that can be used to interact with
        the database.
    """
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


def get_db_session():
    """
    Returns a database session for use in repositories
    """
    return SessionLocal()
