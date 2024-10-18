"""
Application configuration module.

This module contains the configuration settings for the application,
including database connection details and SQLAlchemy settings.
"""

import os

# Load database credentials from environment variables for security
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "acm_education_db")

# Construct the database URI
SQLALCHEMY_DATABASE_URI = f"mysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Disable SQLAlchemy modification tracking for better performance
SQLALCHEMY_TRACK_MODIFICATIONS = False
