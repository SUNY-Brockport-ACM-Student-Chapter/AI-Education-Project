import datetime

from database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Enum


class Teacher(Base):
    __tablename__ = "teacher"

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    User_name = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable =True)
    email = Column(String(120), unique=True, nullable=False)
    clerk_user_id = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'teacher'), default = 'teacher', nullable=False)
    is_active = Column(Boolean, default=False)
    last_login = Column(DateTime, nullable=False, default= datetime.utcnow)
    created_at = Column(DateTime, nullable=False, default= datetime.utcnow)
    updated_at = Column(DateTime, nullabel=False, defualt= datetime.utcnow)

    def __repr__(self):
        return f"<Teacher(user_name = {self.user_name}, email = {self.email})>"

    