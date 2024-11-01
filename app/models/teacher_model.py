# models/teacher_model.py

import datetime
from datetime import timezone

from sqlalchemy import Boolean, Column, DateTime, Enum, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Teacher(Base):
    """
    Represents a teacher in the system.

    Attributes:
        teacher_id (int): Primary key, auto-incrementing identifier
        User_name (str): Unique username/netID, max 50 characters
        first_name (str): Teacher's first name, max 32 characters
        last_name (str): Teacher's last name, max 32 characters
        email (str): Unique email address, max 120 characters
        clerk_user_id (str): External authentication ID
        role (enum): User role ('admin' or 'teacher')
        is_active (bool): Whether the account is active
        last_login (datetime): Timestamp of last login
        created_at (datetime): Timestamp of when the record was created
        updated_at (datetime): Timestamp of when the record was last updated
    """

    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    User_name = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    clerk_user_id = Column(String(255), nullable=False)
    role = Column(Enum("admin", "teacher"), default="teacher", nullable=False)
    is_active = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=False, default=datetime.datetime.now(timezone.utc))
    created_at = Column(DateTime, default=lambda: datetime.datetime.now(timezone.utc))
    updated_at = Column(
        DateTime, 
        default=lambda: datetime.datetime.now(timezone.utc), 
        onupdate=lambda: datetime.datetime.now(timezone.utc)
    )

    # Add relationship to Course
    courses = relationship("Course", back_populates="teacher")

    def __repr__(self):
        return f"<Teacher(user_name = {self.User_name}, email = {self.email})>"
