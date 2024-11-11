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

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config import SQLALCHEMY_DATABASE_URI

# Load environment variables
load_dotenv()

# Create base class for declarative models
Base = declarative_base()

# Database URL configuration
SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URI

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db(app):
    # Create the database engine
    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])

    # Create all tables in the database (if they don't exist)
    Base.metadata.create_all(engine)

    # Bind the engine to the session
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Optionally, you can set the session to the app context
    app.session = SessionLocal()


def get_db_session():
    return SessionLocal()
