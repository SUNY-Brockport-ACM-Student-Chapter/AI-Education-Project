# models/user_model.py

import datetime
from datetime import timezone

from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base, role_enum  # Import the enum we created


class User(Base):
    """
    Represents a user in the system.

    Attributes:
        user_id (int): Primary key, auto-incrementing identifier
        user_name (str): Unique username/netID, max 50 characters
        first_name (str): Teacher's first name, max 32 characters
        last_name (str): Teacher's last name, max 32 characters
        email (str): Unique email address, max 120 characters
        clerk_user_id (str): External authentication ID
        role (enum): Role represents a user's role: admin or user
        is_active (bool): Whether the account is active
        last_login (datetime): Timestamp of last login
        created_at (datetime): Timestamp of when the record was created
        updated_at (datetime): Timestamp of when the record was last updated
    """

    __tablename__ = "user"

    user_id = Column(String(12), primary_key=True, autoincrement=True) #ID_REFERENCE
    email = Column(String(120), unique=True, nullable=False)
    clerk_id = Column(String(255), nullable=False)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=True)
    is_active = Column(Boolean, default=False)
    last_login = Column(
        DateTime, nullable=False, default=datetime.datetime.now(timezone.utc)
    )
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(timezone.utc))
    updated_at = Column(
        DateTime,
        default=lambda: datetime.datetime.now(timezone.utc),
        onupdate=lambda: datetime.datetime.now(timezone.utc),
    )

    # Add relationship to Course
    courses = relationship(
        "Course", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Teacher(user_name = {self.user_name}, email = {self.email})>"

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
        }
