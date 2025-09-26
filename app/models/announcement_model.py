# models/announcement_model.py
from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base


class Announcement(Base):
    """
    Represents an announcement within a course section.

    Attributes:
        announcement_id (str): Primary key, unique identifier.
        section_id (str): Foreign key linking to the parent section.
        title (str): The title of the announcement.
        body (str): The content of the announcement.
        author_id (str): Foreign key linking to the user who created the announcement.
        pinned (bool): Indicates if the announcement is pinned.
        created_at (datetime): Timestamp of creation.
        updated_at (datetime): Timestamp of last update.
    """

    __tablename__ = "announcement"

    announcement_id = Column(String(12), primary_key=True) #ID_REFERENCE
    section_id = Column(String(12), ForeignKey("section.section_id"), nullable=False) #ID_REFERENCE
    title = Column(String, nullable=False)
    body = Column(String, nullable=False)
    author_id = Column(String(12), ForeignKey("user.user_id"), nullable=True) #ID_REFERENCE
    pinned = Column(Boolean, default=False, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc), nullable=False)

    # Relationships
    section = relationship("Section", back_populates="announcements")
    author = relationship("User", back_populates="announcements")

    def __repr__(self):
        return f"<Announcement(id='{self.announcement_id}', title='{self.title}')>"

    def to_dict(self):
        return {
            "announcement_id": self.announcement_id,
            "section_id": self.section_id,
            "title": self.title,
            "body": self.body,
            "author_id": self.author_id,
            "pinned": self.pinned,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
