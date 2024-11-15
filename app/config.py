"""
config.py

This module contains the configuration settings for the application,
including database connection details and SQLAlchemy settings.

Environment Variables:
- MYSQL_USER: The username for the MySQL database.
- MYSQL_PASSWORD: The password for the MySQL database.
- MYSQL_HOST: The host address of the MySQL database.
- MYSQL_DB: The name of the MySQL database.

Configuration Constants:
- SQLALCHEMY_DATABASE_URI: The URI for connecting to the MySQL database.
- SQLALCHEMY_TRACK_MODIFICATIONS: A flag to disable SQLAlchemy
- modification tracking for better performance.
"""

import os

from dotenv import load_dotenv

# Construct the database URI
load_dotenv()
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_DB = os.getenv("MYSQL_DB")

SQLALCHEMY_DATABASE_URI = (
    f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
)

# Disable SQLAlchemy modification tracking for better performance
SQLALCHEMY_TRACK_MODIFICATIONS = False
