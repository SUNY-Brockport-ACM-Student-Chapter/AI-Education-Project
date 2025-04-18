# models/enrollment_model.py

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Enum
from sqlalchemy.orm import relationship

from app.database import Base, EnrollmentStatusEnum


class Enrollment(Base):
    """
    Represents a student's enrollment in a course.

    Attributes:
        enrollment_id (int): Primary key, auto-incrementing identifier
        student_id (int): Foreign key referencing the enrolled student
        course_id (int): Foreign key referencing the course
        status (enum): Current enrollment status ('enrolled', 'cancelled', 'pending')
        enrollment_date (datetime): When the enrollment occurred
    """

    __tablename__ = "Enrollment"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("Student.student_id"), nullable=False)
    course_id = Column(Integer, ForeignKey("Course.course_id"), nullable=False)
    status = Column(Enum(EnrollmentStatusEnum), default=EnrollmentStatusEnum.enrolled)
    enrollment_date = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    student = relationship("Student", back_populates="enrollment")
    course = relationship("Course", back_populates="enrollment")

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"

    def to_dict(self):
        return {
            "enrollment_id": self.enrollment_id,
            "student_id": self.student_id,
            "course_id": self.course_id,
            "status": self.status.value if self.status else None,
            "enrollment_date": self.enrollment_date.isoformat(),
        }
