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
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variables
load_dotenv()

# Create base class for declarative models
Base = declarative_base()

# Database URL configuration
SQLALCHEMY_DATABASE_URL = (
    f"mysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
    f"@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"
)

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db_session():
    return SessionLocal()
