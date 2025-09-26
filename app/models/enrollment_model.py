# models/enrollment_model.py

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.database import Base, enrollment_status_enum  # Import the enum we created


class Enrollment(Base):
    """
    Represents a student's enrollment in a course.

    Attributes:
        enrollment_id (int): Primary key, auto-incrementing identifier
        student_id (int): Foreign key referencing the enrolled student
        section_id (int): Foreign key referencing the course
        status (enum): Current enrollment status ('enrolled', 'cancelled', 'pending')
        enrollment_date (datetime): When the enrollment occurred
    """

    __tablename__ = "enrollment"

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(12), ForeignKey("student.student_id"), nullable=False) #ID_REFERENCE
    section_id = Column(String(12), ForeignKey("section.section_id"), nullable=False)
    role = Column(Enum("student", "ta", "teacher", name="section_role_enum"), nullable=False)
    status = Column(Enum("enrolled", "pending", "dropped", "banned", name="enrollment_status_enum"), default="enrolled")  # Use the proper enum
    joined_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    dropped_at = Column(DateTime)
    user = relationship("User", back_populates="enrollment")
    section = relationship("Section", back_populates="enrollment")

    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, section_id={self.section_id})>"

    def to_dict(self):
        return {
            "enrollment_id": self.enrollment_id,
            "student_id": self.student_id,
            "section_id": self.section_id,
            "status": self.status,
            "enrollment_date": self.enrollment_date.isoformat(),
        }

 