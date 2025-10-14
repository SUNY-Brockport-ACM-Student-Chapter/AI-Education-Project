# models/rubric_rating_model.py
from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class RubricRating(Base):
    """
    Represents a rating level within a rubric criterion.

    Attributes:
        id (str): Primary key, unique identifier for the rating.
        criterion_id (str): Foreign key linking to the parent criterion.
        level (str): The level of achievement (e.g., "Exceeds Expectations", "Meets Expectations").
        description (str): A detailed description of the rating level.
        points (float): The points awarded for this rating level.
    """

    __tablename__ = "rubric_rating"

    rubric_rating_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    criterion_id = Column(UUID(as_uuid=True), ForeignKey("rubric_criterion.rubric_criterion_id"), nullable=False) #ID_REFERENCE
    level = Column(String, nullable=False)
    description = Column(String)
    points = Column(Float, nullable=False)

    # Relationships
    criterion = relationship("RubricCriterion", back_populates="ratings")
    scores = relationship("RubricScore", back_populates="rating")
    

    def __repr__(self):
        return f"<RubricRating(level='{self.level}', points={self.points})>"

    def to_dict(self):
        return {
            "rubric_rating_id": self.rubric_rating_id,
            "criterion_id": self.criterionId,
            "level": self.level,
            "description": self.description,
            "points": self.points,
        }
