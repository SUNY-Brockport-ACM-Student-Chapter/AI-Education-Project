"""
Application configuration module.

This module contains the configuration settings for the application,
including database connection details and SQLAlchemy settings.
"""

import os

# Construct the database URI
SQLALCHEMY_DATABASE_URI = f"mysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DB')}"

# Disable SQLAlchemy modification tracking for better performance
SQLALCHEMY_TRACK_MODIFICATIONS = False
