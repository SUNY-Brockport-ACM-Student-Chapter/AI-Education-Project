# services/student_service.py

from app.models.student_model import Student
from app.repositories.student_repository import StudentRepository



class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def get_dashboard_data(self, student_id: int):
        student = self.get_student_by_id(student_id)
        courses = self.get_all_courses_for_student(student.student_id)
        exams = self.get_all_exams_for_student(student.student_id)
        teachers = [course.teacher for course in courses]


        return {
            "courses": [course.to_dict() for course in courses],
            "exams": [exam.to_dict() for exam in exams],
            "teachers": [teacher.to_dict() for teacher in teachers],
            "student": student.to_dict()
        }

    def get_exam_list(self, student_id: int):
        student = self.get_student_by_id(student_id)
        exams = self.get_all_exams_for_student(student.student_id)
        return [exam.to_dict() for exam in exams]


    def get_student_by_id(self, student_id: int):
        return self.student_repo.get_student_by_id(student_id)

    def get_all_courses_for_student(self, student_id: int):
        return self.student_repo.get_all_courses_for_student(student_id)

    def get_all_exams_for_student(self, student_id: int):
        return self.student_repo.get_all_exams_for_student(student_id)
    
    def get_student_by_clerk_user_id(self, clerk_user_id: str):
        return self.student_repo.get_student_by_clerk_user_id(clerk_user_id)
    

    def get_all_students(self):
        return self.student_repo.get_all_students()

    def create_student(self, student: Student):
        return self.student_repo.create_student(student)

    def update_student(self, student: Student):
        return self.student_repo.update_student(student)

    def delete_student(self, student: Student):
        return self.student_repo.delete_student(student)

    def get_student_by_clerk_id(self, clerk_user_id: str):
        return self.student_repo.get_student_by_clerk_id(clerk_user_id)
