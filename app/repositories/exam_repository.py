# repositories/exam_repository.py

from sqlalchemy.orm import Session

from models import Exam


class ExamRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_exam_by_id(self, exam_id: int):
        return self.session.query(Exam).filter(Exam.id == exam_id).first()

    def get_all_exams(self):
        return self.session.query(Exam).all()

    def create_exam(self, exam: Exam):
        self.session.add(exam)
        self.session.commit()
        return exam

    def update_exam(self, exam: Exam):
        self.session.merge(exam)
        self.session.commit()
        return exam

    def delete_exam(self, exam: Exam):
        self.session.delete(exam)
        self.session.commit()
