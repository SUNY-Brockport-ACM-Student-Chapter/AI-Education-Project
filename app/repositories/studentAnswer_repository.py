# repositories/studentAnswer_repository.py

from sqlalchemy.orm import Session

from app.models.studentAnswer_model import StudentAnswer


class StudentAnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_student_answers_for_student(self, student_id: int, question_id: int):
        return self.session.query(StudentAnswer).filter(StudentAnswer.student_id == student_id, StudentAnswer.question_id == question_id).all()
    
    def create_student_answer(self, student_id: int, question_id: int):
        new_student_answer = StudentAnswer(student_id=student_id, question_id=question_id)
        self.session.add(new_student_answer)
        self.session.commit()
        return new_student_answer

    def get_student_answer_by_id(self, student_answer_id: int):
        return self.session.query(StudentAnswer).filter(StudentAnswer.student_answer_id == student_answer_id).first()

