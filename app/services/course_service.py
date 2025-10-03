# services/course_service.py

from app.models.course_model import Course
# Removed unused 'Assessment' model import
from app.repositories.course_repository import CourseRepository
from typing import Optional, List

# Standardizing resource IDs to string (UUIDs)
ID_TYPE = str


class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def get_course_by_id(self, course_id: ID_TYPE) -> Optional[Course]:
        """Retrieves a single course by its ID."""
        return self.course_repo.get_course_by_id(course_id)
        
    def delete_course(self, course_id: ID_TYPE) -> bool:
        """Deletes a single course by its ID."""
        return self.course_repo.delete_course(course_id)

    def get_active_courses_for_teacher(self, teacher_id: ID_TYPE) -> List[Course]:
        """Retrieves all active courses taught by the given teacher."""
        return self.course_repo.get_active_courses_for_teacher(teacher_id)

    def create_course(self, teacher_id: ID_TYPE, course_data: dict) -> Course:
        """Creates a new course."""
        # Teacher ID is part of the context, but included here for clarity
        return self.course_repo.create_course(teacher_id, course_data)

    def update_course(self, course_id: ID_TYPE, course_data: dict) -> Course:
        """Updates an existing course."""
        return self.course_repo.update_course(course_id, course_data)

    def change_course_status(self, course_id: ID_TYPE) -> Course:
        """Toggles the active status of a course."""
        return self.course_repo.change_course_status(course_id)

    def get_active_courses_for_student(self, student_id: ID_TYPE) -> List[Course]:
        """Retrieves all active courses the given student is enrolled in."""
        return self.course_repo.get_active_courses_for_student(student_id)
