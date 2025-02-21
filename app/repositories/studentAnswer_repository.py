# repositories/studentAnswer_repository.py

from sqlalchemy.orm import Session

from app.models.question_model import Question
from app.models.student_model import Student
from app.models.studentAnswer_model import StudentAnswer


class StudentAnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_student_answers_for_student(self, student_id: int, question_id: int):
        student_answers = (
            self.session.query(StudentAnswer)
            .filter(
                StudentAnswer.student_id == student_id,
                StudentAnswer.question_id == question_id,
            )
            .all()
        )
        if not student_answers:
            raise ValueError("No student answers found")
        return student_answers

    def create_student_answer(self, student_id: int, question_id: int, data: dict):
        student = self.session.query(Student).filter(Student.id == student_id).first()
        if not student:
            raise ValueError("Student not found")
        question = (
            self.session.query(Question).filter(Question.id == question_id).first()
        )
        if not question:
            raise ValueError("Question not found")
        new_student_answer = StudentAnswer(
            student_id=student_id, question_id=question_id, **data
        )
        self.session.add(new_student_answer)
        self.session.commit()
        return new_student_answer
