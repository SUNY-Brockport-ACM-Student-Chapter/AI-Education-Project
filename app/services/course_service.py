# services/course_service.py

from app.models.course_model import Course
from app.repositories.course_repository import CourseRepository
from app.models.exam_model import Exam


class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def get_active_courses_for_teacher(self, teacher_id: int):
        return self.course_repo.get_active_courses_for_teacher(teacher_id)
    
    def create_course(self, teacher_id: int, course_data: dict):
        return self.course_repo.create_course(teacher_id, course_data)
    
    def update_course(self, course_id: int, course_data: dict):
        return self.course_repo.update_course(course_id, course_data)
    
    def change_course_status(self, course_id: int):
        return self.course_repo.change_course_status(course_id)
    
    def get_active_courses_for_student(self, student_id: int):
        return self.course_repo.get_active_courses_for_student(student_id)
