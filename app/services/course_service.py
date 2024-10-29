# services/course_service.py

from app.models.course_model import Course
from app.repositories.course_repository import CourseRepository


class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def get_course_by_id(self, course_id: int):
        return self.course_repo.get_course_by_id(course_id)

    def get_all_courses(self):
        return self.course_repo.get_all_courses()

    def create_course(self, course: Course):
        return self.course_repo.create_course(course)

    def update_course(self, course: Course):
        return self.course_repo.update_course(course)

    def delete_course(self, course: Course):
        return self.course_repo.delete_course(course)
