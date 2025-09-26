# models/file_object_model.py
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class FileObject(Base):
    """
    Represents a file uploaded to the system.

    Attributes:
        file_object_id (str): Primary key, unique identifier.
        owner_id (str): Foreign key to the user who owns the file (nullable).
        section_id (str): Foreign key to the section the file belongs to (nullable).
        assessment_id (str): Foreign key to the assessment the file belongs to (nullable).
        submission_id (str): Foreign key to the submission the file belongs to (nullable).
        question_id (str): Foreign key to the question the file belongs to (nullable).
        feedback_id (str): Foreign key to the feedback the file belongs to (nullable).
        uri (str): The URI or path to the file.
        file_name (str): The original name of the file.
        mime_type (str): The MIME type of the file.
        size_bytes (int): The size of the file in bytes.
        created_at (datetime): Timestamp of creation.
    """

    __tablename__ = "file_object"

    file_object_id = Column(String(12), primary_key=True) #ID_REFERENCE
    owner_id = Column(String(12), ForeignKey("user.user_id"), nullable=True) #ID_REFERENCE
    section_id = Column(String(12), ForeignKey("section.section_id"), nullable=True) #ID_REFERENCE
    assessment_id = Column(String(12), ForeignKey("assessment.assessment_id"), nullable=True) #ID_REFERENCE
    submission_id = Column(String(12), ForeignKey("submission.submission_id"), nullable=True) #ID_REFERENCE
    question_id = Column(String(12), ForeignKey("question.question_id"), nullable=True) #ID_REFERENCE
    feedback_id = Column(String(12), ForeignKey("feedback.feedback_id"), nullable=True) #ID_REFERENCE
    uri = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    mime_type = Column(String, nullable=False)
    size_bytes = Column(Integer)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    owner = relationship("User", back_populates="file_objects")
    section = relationship("Section", back_populates="file_objects")
    assessment = relationship("Assessment", back_populates="file_objects")
    submission = relationship("Submission", back_populates="file_objects")
    question = relationship("Question", back_populates="file_objects")
    feedback = relationship("Feedback", back_populates="file_objects")

    def __repr__(self):
        return f"<FileObject(id='{self.file_object_id}', file_name='{self.file_name}')>"

    def to_dict(self):
        return {
            "file_object_id": self.file_object_id,
            "owner_id": self.owner_id,
            "section_id": self.section_id,
            "assessment_id": self.assessment_id,
            "submission_id": self.submission_id,
            "question_id": self.question_id,
            "feedback_id": self.feedback_id,
            "uri": self.uri,
            "file_name": self.file_name,
            "mime_type": self.mime_type,
            "size_bytes": self.size_bytes,
            "created_at": self.created_at.isoformat(),
        }
