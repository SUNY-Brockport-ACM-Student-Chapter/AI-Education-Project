# services/teacher_service.py

from app.models.teacher_model import Teacher
from app.repositories.teacher_repository import TeacherRepository


class TeacherService:
    def __init__(self, teacher_repo: TeacherRepository):
        self.teacher_repo = teacher_repo

    def get_dashboard_data(self, teacher_id: int):
        teacher = self.get_teacher_by_id(teacher_id)
        courses = self.get_all_courses_for_teacher(teacher.teacher_id)
        exams = self.get_all_exams_for_teacher(teacher.teacher_id)

        return {
            "courses": [course.to_dict() for course in courses],
            "exams": [exam.to_dict() for exam in exams],
            "teacher": teacher.to_dict()
        }
    
    def search_for_student(self, search_query: str):
        return self.teacher_repo.search_for_student(search_query)
    
    def get_teacher_by_clerk_user_id(self, clerk_user_id: str):
        return self.teacher_repo.get_teacher_by_clerk_user_id(clerk_user_id)
    
    def get_all_courses_for_teacher(self, teacher_id: int):
        return self.teacher_repo.get_all_courses_for_teacher(teacher_id)
    
    def get_all_exams_for_teacher(self, teacher_id: int):
        return self.teacher_repo.get_all_exams_for_teacher(teacher_id)

    def get_all_active_courses_for_teacher(self, teacher_id: int):
        return self.teacher_repo.get_all_active_courses(teacher_id)
    
    def get_all_inactive_courses_for_teacher(self, teacher_id: int):
        return self.teacher_repo.get_all_inactive_courses(teacher_id)


    def get_teacher_by_id(self, teacher_id: int):
        return self.teacher_repo.get_teacher_by_id(teacher_id)

    def get_all_teachers(self):
        return self.teacher_repo.get_all_teachers()

    def create_teacher(self, teacher: Teacher):
        return self.teacher_repo.create_teacher(teacher)

    def update_teacher(self, teacher: Teacher):
        return self.teacher_repo.update_teacher(teacher)

    def delete_teacher(self, teacher: Teacher):
        return self.teacher_repo.delete_teacher(teacher)
