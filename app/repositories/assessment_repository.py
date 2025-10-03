# repositories/assessment_repository.py

from sqlalchemy.orm import Session

from app.models.course_model import Course
from app.models.section_model import Section
from app.models.assessment_model import Assessment
from app.models.question_model import Question
from app.models.user_model import User
from app.models.submission_model import Submission

class AssessmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_assessment_by_id(self, assessment_id: int):
        assessment = self.session.query(Assessment).filter(Assessment.assessment_id == assessment_id).first()
        if not assessment:
            raise ValueError("Assessment not found")
        return assessment

    def get_assessments_for_teacher(self, teacher_id: int):
        teacher = (
            self.session.query(User).filter(User.teacher_id == teacher_id).first()
        )
        if not teacher:
            raise ValueError("User not found")
        courses = (
            self.session.query(Course).filter(Course.teacher_id == teacher_id).all()
        )
        assessments = []
        for course in courses:
            assessments.extend(
                self.session.query(Assessment)
                .filter(Assessment.course_id == course.course_id)
                .all()
            )
        return assessments

    def get_assessments_for_course(self, course_id: int):
        course = (
            self.session.query(Course).filter(Course.course_id == course_id).first()
        )
        if not course:
            raise ValueError("Course not found")
        assessments = self.session.query(Assessment).filter(Assessment.course_id == course_id).all()
        return assessments

    def create_assessment(self, course_id: int, data: dict):
        course = (
            self.session.query(Course).filter(Course.course_id == course_id).first()
        )
        if not course:
            raise ValueError("Course not found")
        new_assessment = Assessment(course_id=course_id, **data)
        self.session.add(new_assessment)
        self.session.commit()
        return new_assessment

    def get_student_assessment_submission_stage(self, assessment_id: int, student_id: int):
        assessment = self.get_assessment_by_id(assessment_id)
        if not assessment:
            raise ValueError("Assessment not found")
        student = (
            self.session.query(User).filter(User.student_id == student_id).first()
        )
        if not student:
            raise ValueError("User not found")
        first_assessment_question = (
            self.session.query(Question).filter(Question.assessment_id == assessment_id).first()
        )
        if not first_assessment_question:
            raise ValueError("Assessment question not found")
        student_answer = (
            self.session.query(StudentAnswer)
            .filter(
                StudentAnswer.student_id == student_id,
                StudentAnswer.question_id == first_assessment_question.question_id,
            )
            .first()
        )
        if not student_answer:
            return 0
        return student_answer.answer_stage

    def get_assessments_for_student(self, student_id: int):
        student = (
            self.session.query(User).filter(User.student_id == student_id).first()
        )
        if not student:
            raise ValueError("User not found")
        enrollments = (
            self.session.query(Section)
            .filter(Section.student_id == student_id)
            .all()
        )
        if not enrollments:
            raise ValueError("User not enrolled in any sections")
        course_ids = [enrollment.course_id for enrollment in enrollments]
        assessments = self.session.query(Assessment).filter(Assessment.course_id.in_(course_ids)).all()
        return assessments

    def get_questions_for_assessment(self, assessment_id: int):
        assessment = self.session.query(Assessment).filter(Assessment.assessment_id == assessment_id).first()
        if not assessment:
            raise ValueError("Assessment not found")
        return self.session.query(Question).filter(Question.assessment_id == assessment_id).all()
