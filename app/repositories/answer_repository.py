# repositories/answer_repository.py

from sqlalchemy.orm import Session

from app.models.answer_model import Answer


class AnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def save_answer(self, question_id: int, answer: str):
        new_answer = Answer(question_id=question_id, answer_text=answer)
        self.session.add(new_answer)
        self.session.commit()

    def get_answer_by_id(self, answer_id: int):
        return self.session.query(Answer).filter(Answer.id == answer_id).first()

    def get_all_answers(self):
        return self.session.query(Answer).all()

    def create_answer(self, answer: Answer):
        self.session.add(answer)
        self.session.commit()
        return answer

    def update_answer(self, answer: Answer):
        self.session.merge(answer)
        self.session.commit()
        return answer

    def delete_answer(self, answer: Answer):
        self.session.delete(answer)
        self.session.commit()
