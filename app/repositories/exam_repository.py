# repositories/exam_repository.py

from datetime import datetime, timezone

from sqlalchemy import and_
from sqlalchemy.orm import Session

from app.models.enrollment_model import Enrollment
from app.models.exam_model import Exam


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

    def get_upcoming_exams_for_student(self, student_id: int):
        """
        Get all upcoming exams for a specific student.

        Args:
            student_id (int): The ID of the student

        Returns:
            List[Dict]: List of upcoming exams as dictionaries, ordered by start date
        """
        current_datetime = datetime.now(timezone.utc)

        exams = (
            self.session.query(Exam)
            .join(Enrollment, Exam.course_id == Enrollment.course_id)
            .filter(
                Enrollment.student_id == student_id,
                Exam.end_date >= current_datetime.replace(tzinfo=None),
            )
            .order_by(Exam.start_date.asc())
            .all()
        )

        # Use the to_dict() method we defined in the Exam model
        return [
            {
                "id": exam.exam_id,
                "course_id": exam.course_id,
                "name": exam.exam_name,
                "start_date": exam.start_date,
                "end_date": exam.end_date,
                "exam_description": exam.exam_description,
            }
            for exam in exams
        ]
