# services/exam_service.py

from app.repositories.exam_repository import ExamRepository


class ExamService:
    def __init__(self, exam_repo: ExamRepository):
        self.exam_repo = exam_repo
    
    def get_exams_for_teacher(self, teacher_id: int):
        return self.exam_repo.get_exams_for_teacher(teacher_id)
    
    def get_exams_for_course(self, course_id: int):
        return self.exam_repo.get_exams_for_course(course_id)
    
    def create_exam(self, course_id: int):
        return self.exam_repo.create_exam(course_id)
    
    def get_exam_submission_number(self, exam_id: int, student_id: int):
        return self.exam_repo.get_exam_submission_number(exam_id, student_id)
    
    def get_exams_for_student(self, student_id: int):   
        return self.exam_repo.get_exams_for_student(student_id)
