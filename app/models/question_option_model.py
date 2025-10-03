# models/question_option_model.py
from sqlalchemy import Boolean, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from app.database import Base


class QuestionOption(Base):
    """
    Represents a single option for a multiple-choice question.

    Attributes:
        question_option_id (str): Primary key, unique identifier.
        question_id (str): Foreign key linking to the parent question.
        label (str): Optional label for the option (e.g., 'A', 'B', 'C').
        text (str): The text of the option.
        value (str): The value associated with the option.
        is_correct (bool): Indicates if this is the correct option.
        order_index (int): The display order of the option.
    """

    __tablename__ = "question_option"

    question_option_id = Column(UUID(as_uuid=True), primary_key=True) #ID_REFERENCE
    question_id = Column(UUID(as_uuid=True), ForeignKey("question.question_id"), nullable=False) #ID_REFERENCE
    label = Column(String)
    text = Column(String, nullable=False)
    value = Column(String)
    is_correct = Column(Boolean, nullable=False)
    order_index = Column(Integer)

    # Relationships
    question = relationship("Question", back_populates="options")

    def __repr__(self):
        return f"<QuestionOption(id='{self.question_option_id}', question_id='{self.question_id}')>"

    def to_dict(self):
        return {
            "question_option_id": self.question_option_id,
            "question_id": self.question_id,
            "label": self.label,
            "text": self.text,
            "value": self.value,
            "is_correct": self.is_correct,
            "order_index": self.order_index,
        }
