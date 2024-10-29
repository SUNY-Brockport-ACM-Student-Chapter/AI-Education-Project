# repositories/question_repository.py

from sqlalchemy.orm import Session

from models import Question


class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_question_by_id(self, question_id: int):
        return self.session.query(Question).filter(Question.id == question_id).first()

    def get_all_questions(self):
        return self.session.query(Question).all()

    def create_question(self, question: Question):
        self.session.add(question)
        self.session.commit()
        return question

    def update_question(self, question: Question):
        self.session.merge(question)
        self.session.commit()
        return question

    def delete_question(self, question: Question):
        self.session.delete(question)
        self.session.commit()
