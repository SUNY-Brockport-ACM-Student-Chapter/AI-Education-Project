"""
config.py

This module contains the configuration settings for the application,
including database connection details and SQLAlchemy settings.

Environment Variables for MySQL:
- MYSQL_USER: The username for the MySQL database.
- MYSQL_PASSWORD: The password for the MySQL database.
- MYSQL_HOST: The host address of the MySQL database.
- MYSQL_DB: The name of the MySQL database.

Environment Variables for PostgreSQL:
- PGHOST: The host address of the PostgreSQL database.
- PGDATABASE: The name of the PostgreSQL database.
- PGUSER: The username for the PostgreSQL database.
- PGPASSWORD: The password for the PostgreSQL database.

Configuration Constants:
- SQLALCHEMY_DATABASE_URI: The URI for connecting to the MySQL or PostgreSQL database.
- SQLALCHEMY_TRACK_MODIFICATIONS: A flag to disable SQLAlchemy
- modification tracking for better performance.
"""

import os

from dotenv import load_dotenv

load_dotenv()


# Commented out MySQL configuration
# MYSQL_USER = os.getenv("MYSQL_USER")
# MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
# MYSQL_HOST = os.getenv("MYSQL_HOST")
# MYSQL_DB = os.getenv("MYSQL_DB")
#
# SQLALCHEMY_DATABASE_URI = (
#     f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
# )


# PostgreSQL connection details
PG_HOST = os.getenv("PGHOST")
PG_DATABASE = os.getenv("PGDATABASE")
PG_USER = os.getenv("PGUSER")
PG_PASSWORD = os.getenv("PGPASSWORD")

# Construct the PostgreSQL database URI
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DATABASE}"
)

# Disable SQLAlchemy modification tracking for better performance
SQLALCHEMY_TRACK_MODIFICATIONS = False
