# repositories/studentAnswer_repository.py

from sqlalchemy.orm import Session

from models import StudentAnswer


class StudentAnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_student_answer_by_id(self, student_answer_id: int):
        return (
            self.session.query(StudentAnswer)
            .filter(StudentAnswer.id == student_answer_id)
            .first()
        )

    def get_all_student_answers(self):
        return self.session.query(StudentAnswer).all()

    def create_student_answer(self, student_answer: StudentAnswer):
        self.session.add(student_answer)
        self.session.commit()
        return student_answer

    def update_student_answer(self, student_answer: StudentAnswer):
        self.session.merge(student_answer)
        self.session.commit()
        return student_answer

    def delete_student_answer(self, student_answer: StudentAnswer):
        self.session.delete(student_answer)
        self.session.commit()
