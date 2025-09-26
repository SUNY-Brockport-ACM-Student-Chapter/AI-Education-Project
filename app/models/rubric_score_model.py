# models/rubric_score_model.py
from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from app.database import Base


class RubricScore(Base):
    """
    Represents a single score given for a rubric criterion on a submission.

    Attributes:
        rubric_score_id (str): Primary key, unique identifier for the score.
        submission_id (str): Foreign key linking to the parent submission.
        criterion_id (str): Foreign key linking to the specific criterion being scored.
        rating_id (str): Foreign key linking to the chosen rating level (nullable).
        points_awarded (float): The points awarded for this criterion.
        comment (str): Optional comments from the grader.
    """

    __tablename__ = "rubric_score"

    rubric_score_id = Column(String(12), primary_key=True) #ID_REFERENCE
    submission_id = Column(String(12), ForeignKey("submission.submission_id"), nullable=False) #ID_REFERENCE
    criterion_id = Column(String(12), ForeignKey("rubric_criterion.rubric_criterion_id"), nullable=False) #ID_REFERENCE
    rating_id = Column(String(12), ForeignKey("rubric_rating.rubric_rating_id"), nullable=True) #ID_REFERENCE
    points_awarded = Column(Float, nullable=False)
    comment = Column(String)

    # Relationships
    submission = relationship("Submission", back_populates="rubric_scores")
    criterion = relationship("RubricCriterion", back_populates="scores")
    rating = relationship("RubricRating", back_populates="scores")

    def __repr__(self):
        return f"<RubricScore(criterion_id='{self.criterion_id}', points_awarded={self.points_awarded})>"

    def to_dict(self):
        return {
            "rubric_score_id": self.rubric_score_id,
            "submission_id": self.submission_id,
            "criterion_id": self.criterion_id,
            "rating_id": self.rating_id,
            "points_awarded": self.points_awarded,
            "comment": self.comment,
        }
