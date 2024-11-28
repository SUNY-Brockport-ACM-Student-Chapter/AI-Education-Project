# services/exam_service.py

from app.models.exam_model import Exam
from app.models.question_model import Question
from app.repositories.exam_repository import ExamRepository


class ExamService:
    def __init__(self, exam_repo: ExamRepository):
        self.exam_repo = exam_repo

    def get_exam_by_id(self, exam_id: int):
        return self.exam_repo.get_exam_by_id(exam_id)

    def get_all_exams(self):
        return self.exam_repo.get_all_exams()

    def create_exam(self, exam: Exam):
        return self.exam_repo.create_exam(exam)

    def update_exam(self, exam: Exam):
        return self.exam_repo.update_exam(exam)

    def delete_exam(self, exam: Exam):
        return self.exam_repo.delete_exam(exam)

    def get_upcoming_exams_for_student(self, student_id: int):
        """
        Get all upcoming exams for a specific student.
        Only returns exams that:
        1. Are for courses the student is enrolled in
        2. Haven't ended yet
        3. Are ordered by start date
        """
        return self.exam_repo.get_upcoming_exams_for_student(student_id)
    
    def add_question_to_exam(self, question: Question):
        return self.exam_repo.add_question_to_exam(question)

    def get_course_exams(self, course_id):
        """
        Retrieves all exams for a specific course.

        Args:
            course_id: The ID of the course

        Returns:
            List of exam objects for the specified course
        """
        return self.exam_repo.get_course_exams(course_id)
