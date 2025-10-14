# models/rubric_criterion_model.py
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class RubricCriterion(Base):
    """
    Represents a single criterion within a grading rubric.

    Attributes:
        id (str): Primary key, unique identifier for the criterion.
        rubric_id (str): Foreign key linking to the parent rubric.
        name (str): The name of the criterion (e.g., "Content", "Clarity").
        order_index (int): The display order of the criterion.
        max_points (float): The maximum points for this criterion.
    """

    __tablename__ = "rubric_criterion"

    rubric_criterion_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    rubric_id = Column(UUID(as_uuid=True), ForeignKey("rubric.rubric_id"), nullable=False) #ID_REFERENCE
    name = Column(String, nullable=False)
    order_index = Column(Integer)
    max_points = Column(Float, nullable=False)

    # Relationships
    rubric = relationship("Rubric", back_populates="criteria")
    ratings = relationship("RubricRating", back_populates="criterion")
    scores = relationship("RubricScore", back_populates="criterion")

    def __repr__(self):
        return f"<RubricCriterion(name='{self.name}', max_points={self.max_points})>"

    def to_dict(self):
        return {
            "rubric_criterion_id": self.rubric_criterion_id,
            "rubric_id": self.rubric_id,
            "name": self.name,
            "order_index": self.order_index,
            "max_points": self.max_points,
        }
