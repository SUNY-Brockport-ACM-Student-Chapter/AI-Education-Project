# services/student_service.py

from repositories.student_repository import StudentRepository


class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def get_student(self, student_id: int):
        return self.student_repo.get_student_by_id(student_id)

    def list_students(self):
        return self.student_repo.get_all_students()

    def create_new_student(
        self,
        user_name: str,
        first_name: str,
        last_name: str,
        email: str,
        clerk_user_id: str,
    ):
        return self.student_repo.create_student(
            user_name, first_name, last_name, email, clerk_user_id
        )

    def update_existing_student(self, student_id: int, **kwargs):
        return self.student_repo.update_student(student_id, **kwargs)

    def delete_student(self, student_id: int):
        return self.student_repo.delete_student(student_id)
