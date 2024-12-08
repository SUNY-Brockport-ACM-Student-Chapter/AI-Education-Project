# repositories/exam_repository.py

from sqlalchemy.orm import Session

from app.models.course_model import Course
from app.models.enrollment_model import Enrollment
from app.models.exam_model import Exam
from app.models.question_model import Question
from app.models.student_model import Student
from app.models.studentAnswer_model import StudentAnswer
from app.models.teacher_model import Teacher


class ExamRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_exam_by_id(self, exam_id: int):
        exam = self.session.query(Exam).filter(Exam.exam_id == exam_id).first()
        if not exam:
            raise ValueError("Exam not found")
        return exam

    def get_exams_for_teacher(self, teacher_id: int):
        teacher = (
            self.session.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()
        )
        if not teacher:
            raise ValueError("Teacher not found")
        courses = (
            self.session.query(Course).filter(Course.teacher_id == teacher_id).all()
        )
        exams = []
        for course in courses:
            exams.extend(
                self.session.query(Exam)
                .filter(Exam.course_id == course.course_id)
                .all()
            )
        return exams

    def get_exams_for_course(self, course_id: int):
        course = (
            self.session.query(Course).filter(Course.course_id == course_id).first()
        )
        if not course:
            raise ValueError("Course not found")
        exams = self.session.query(Exam).filter(Exam.course_id == course_id).all()
        return exams

    def create_exam(self, course_id: int, data: dict):
        course = (
            self.session.query(Course).filter(Course.course_id == course_id).first()
        )
        if not course:
            raise ValueError("Course not found")
        new_exam = Exam(course_id=course_id, **data)
        self.session.add(new_exam)
        self.session.commit()
        return new_exam

    def get_student_exam_submission_stage(self, exam_id: int, student_id: int):
        exam = self.get_exam_by_id(exam_id)
        if not exam:
            raise ValueError("Exam not found")
        student = (
            self.session.query(Student).filter(Student.student_id == student_id).first()
        )
        if not student:
            raise ValueError("Student not found")
        first_exam_question = (
            self.session.query(Question).filter(Question.exam_id == exam_id).first()
        )
        if not first_exam_question:
            raise ValueError("Exam question not found")
        student_answer = (
            self.session.query(StudentAnswer)
            .filter(
                StudentAnswer.student_id == student_id,
                StudentAnswer.question_id == first_exam_question.question_id,
            )
            .first()
        )
        if not student_answer:
            return 0
        return student_answer.answer_stage

    def get_exams_for_student(self, student_id: int):
        student = (
            self.session.query(Student).filter(Student.student_id == student_id).first()
        )
        if not student:
            raise ValueError("Student not found")
        enrollments = (
            self.session.query(Enrollment)
            .filter(Enrollment.student_id == student_id)
            .all()
        )
        if not enrollments:
            raise ValueError("Student not enrolled in any course")
        course_ids = [enrollment.course_id for enrollment in enrollments]
        exams = self.session.query(Exam).filter(Exam.course_id.in_(course_ids)).all()
        return exams
