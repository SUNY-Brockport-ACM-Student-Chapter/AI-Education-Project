# repositories/answer_repository.py

from sqlalchemy.orm import Session

from app.models.answer_model import Answer
from app.models.question_model import Question


class AnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_answer(self, question_id: int, answer_text: str):
        question = (
            self.session.query(Question)
            .filter(Question.question_id == question_id)
            .first()
        )
        if not question:
            raise ValueError("Question not found")
        new_answer = Answer(question_id=question_id, answer_text=answer_text)
        self.session.add(new_answer)
        self.session.commit()
        return new_answer
