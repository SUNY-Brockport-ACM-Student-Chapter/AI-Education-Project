# models/enrollment_model.py

from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Enrollment(Base):
    """
    Represents a student's enrollment in a course.

    Attributes:
        enrollment_id (int): Primary key, auto-incrementing identifier
        student_id (int): Foreign key referencing the enrolled student
        course_id (int): Foreign key referencing the course
        status (enum): Current enrollment status ('enrolled', 'cancelled', 'padding')
        enrollment_date (datetime): When the enrollment occurred
    """

    __tablename__ = "enrollment"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student.student_id"), nullable=False)
    course_id = Column(Integer, ForeignKey("course.course_id"), nullable=False)
    status = Column(Enum("enrolled", "cancelled", "padding"), default="enrolled")
    enrollment_date = Column(DateTime, nullable=False)

    student = relationship("Student", back_populates="enrollment")
    course = relationship("Course", back_populates="enrollment")

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"
