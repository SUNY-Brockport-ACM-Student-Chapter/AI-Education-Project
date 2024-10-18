# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL can be configured with your actual database URL.
# Example for a local SQLite database:
# SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# Example for a PostgreSQL database:
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Replace with your actual database URL

# Create a new SQLAlchemy engine instance
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a new sessionmaker for handling transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the models to inherit
Base = declarative_base()


# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
