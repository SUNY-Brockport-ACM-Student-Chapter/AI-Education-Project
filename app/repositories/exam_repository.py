# repositories/exam_repository.py

from sqlalchemy.orm import Session

from app.models.enrollment_model import Enrollment
from app.models.exam_model import Exam
from app.models.question_model import Question
from app.models.studentAnswer_model import StudentAnswer


class ExamRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_exam_by_id(self, exam_id: int):
        return self.session.query(Exam).filter(Exam.exam_id == exam_id).first()
    
    def get_exams_for_teacher(self, teacher_id: int):
        return self.session.query(Exam).filter(Exam.teacher_id == teacher_id).all()
    
    def get_exams_for_course(self, course_id: int):
        return self.session.query(Exam).filter(Exam.course_id == course_id).all()
    
    def create_exam(self, course_id: int):
        new_exam = Exam(course_id=course_id)
        self.session.add(new_exam)
        self.session.commit()
        return new_exam
    
    
    def get_exam_submission_number(self, exam_id: int, student_id: int):
        exam_questions = self.session.query(Question).filter(Question.exam_id == exam_id).all()
        student_answers = self.session.query(StudentAnswer).filter(StudentAnswer.student_id == student_id, StudentAnswer.question_id.in_(exam_questions)).all()
        first_answer_id = student_answers[0].student_answer_id
        return first_answer_id.answer_stage
    


    def get_exams_for_student(self, student_id: int):
        return self.session.query(Exam).join(Enrollment).filter(Enrollment.student_id == student_id).all()

    