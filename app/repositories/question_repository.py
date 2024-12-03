# repositories/question_repository.py

from sqlalchemy.orm import Session

from app.models.question_model import Question


class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_questions_for_exam(self, exam_id: int): 
        return self.session.query(Question).filter(Question.exam_id == exam_id).all()
    
    def create_question(self, exam_id: int):
        new_question = Question(exam_id=exam_id)
        self.session.add(new_question)
        self.session.commit()
        return new_question

