# services/course_service.py

from app.models.course_model import Course
from app.repositories.course_repository import CourseRepository
from app.models.exam_model import Exam


class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def get_course_by_id(self, course_id: int):
        return self.course_repo.get_course_by_id(course_id)

    def get_all_courses(self):
        return self.course_repo.get_all_courses()
    
    def get_exams_for_course(self, course_id: int):
        return self.course_repo.get_exams_for_course(course_id)

    def create_course(self, course: Course):
        return self.course_repo.create_course(course)

    def update_course(self, course: Course):
        return self.course_repo.update_course(course)

    def delete_course(self, course: Course):
        return self.course_repo.delete_course(course)
    
    def add_exam_to_course(self, exam: Exam):
        return self.course_repo.add_exam_to_course(exam)
    
    def get_course_info(self, course_id: int):
        return self.course_repo.get_course_info(course_id)

    def get_courses_for_student(self, student_id: int):
        """
        Get all courses that a student is currently enrolled in.
        Returns active courses ordered by course code.
        """
        return self.course_repo.get_courses_for_student(student_id)
