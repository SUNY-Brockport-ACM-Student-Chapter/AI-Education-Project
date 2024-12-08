# repositories/question_repository.py

from sqlalchemy.orm import Session

from app.models.exam_model import Exam
from app.models.question_model import Question


class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_questions_for_exam(self, exam_id: int):
        exam = self.session.query(Exam).filter(Exam.exam_id == exam_id).first()
        if not exam:
            raise ValueError("Exam not found")
        return self.session.query(Question).filter(Question.exam_id == exam_id).all()

    def create_question(self, exam_id: int, data: dict):
        exam = self.session.query(Exam).filter(Exam.exam_id == exam_id).first()
        if not exam:
            raise ValueError("Exam not found")
        new_question = Question(exam_id=exam_id, **data)
        self.session.add(new_question)
        self.session.commit()
        return new_question
