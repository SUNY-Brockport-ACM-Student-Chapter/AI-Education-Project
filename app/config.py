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

Environment Variables for Supabase:
- SB_USER: The username for the Supabase database.
- SB_PASSWORD: The password for the Supabase database.
- SB_HOST: The host address of the Supabase database.
- SB_DATABASE: The name of the Supabase database.
- SB_PORT: The port for the Supabase database (default: 5432)

Configuration Constants:
- SQLALCHEMY_DATABASE_URI: The URI for connecting to the Supabase PostgreSQL database.
- SQLALCHEMY_TRACK_MODIFICATIONS: A flag to disable SQLAlchemy
- modification tracking for better performance.
"""

import os
from urllib.parse import quote_plus

from dotenv import load_dotenv, find_dotenv

# Force reload of .env file
load_dotenv(find_dotenv(), override=True)

def get_required_env_var(name: str) -> str:
    """Get a required environment variable or raise an error if not found."""
    value = os.getenv(name)
    if value is None:
        raise ValueError(f"Required environment variable {name} is not set")
    return value

# MySQL connection details
#MYSQL_USER = os.getenv("MYSQL_USER")
#MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
#MYSQL_HOST = os.getenv("MYSQL_HOST")
#MYSQL_DB = os.getenv("MYSQL_DB")



# Construct the MySQL database URI
# URL encode the password to handle special characters
#encoded_password = quote_plus(MYSQL_PASSWORD)
#SQLALCHEMY_DATABASE_URI = (
#    f"mysql+pymysql://{MYSQL_USER}:{encoded_password}@{MYSQL_HOST}/{MYSQL_DB}"
#
#)

# PostgreSQL connection details
#PG_HOST = os.getenv("PGHOST")
#PG_DATABASE = os.getenv("PGDATABASE")
#PG_USER = os.getenv("PGUSER")
#PG_PASSWORD = os.getenv("PGPASSWORD")

# Construct the PostgreSQL database URI
# SQLALCHEMY_DATABASE_URI = (
#     f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}/{PG_DATABASE}"
# )




# Supabase connection details
try:
    SB_USER = get_required_env_var("SB_USER")
    SB_PASSWORD = get_required_env_var("SB_PASSWORD")
    SB_HOST = get_required_env_var("SB_HOST")
    SB_DATABASE = get_required_env_var("SB_DATABASE")
    SB_PORT = os.getenv("SB_PORT", "5432")  # Default PostgreSQL port

    print(f"Debug - Supabase settings:")
    print(f"User: {SB_USER}")
    print(f"Host: {SB_HOST}")
    print(f"DB: {SB_DATABASE}")
    print(f"Port: {SB_PORT}")

    # Construct the Supabase PostgreSQL database URI
    encoded_password = quote_plus(SB_PASSWORD)
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{SB_USER}:{encoded_password}@{SB_HOST}:{SB_PORT}/{SB_DATABASE}"
    )

except ValueError as e:
    print(f"Error loading environment variables: {e}")
    raise

# Disable SQLAlchemy modification tracking for better performance
SQLALCHEMY_TRACK_MODIFICATIONS = False
