# models/student_model.py

import datetime
from datetime import UTC, datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from database import Base


class Student(Base):
    """
    Represents a student in the system.

    Attributes:
        student_id (int): Primary key, auto-incrementing identifier
        user_name (str): Unique username/netID, max 50 characters
        first_name (str): Student's first name, max 32 characters
        last_name (str): Student's last name, max 32 characters
        email (str): Unique email address, max 120 characters
        clerk_user_id (str): External authentication ID
        is_active (bool): Whether the account is active
        last_login (datetime): Timestamp of last login
        created_at (datetime): Timestamp of when the record was created
        updated_at (datetime): Timestamp of when the record was last updated
    """

    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    clerk_user_id = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=False, default=datetime.now(UTC))
    created_at = Column(DateTime, nullable=False, default=datetime.now(UTC))
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now(UTC), onupdate=datetime.now(UTC)
    )

    def __repr__(self):
        return f"<Student(user_name={self.user_name}, email={self.email})>"