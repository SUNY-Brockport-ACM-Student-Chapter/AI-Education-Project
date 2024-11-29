# repositories/teacher_repository.py

from sqlalchemy.orm import Session

from app.models.teacher_model import Teacher
from app.models.course_model import Course
from app.models.exam_model import Exam
from app.models.student_model import Student

class TeacherRepository:
    def __init__(self, session: Session):
        self.session = session


    def get_teacher_by_clerk_user_id(self, clerk_user_id: str):
        return self.session.query(Teacher).filter(Teacher.clerk_user_id == clerk_user_id).first()
    
    def get_all_courses_for_teacher(self, teacher_id: int):
        return self.session.query(Course).filter(Course.teacher_id == teacher_id).all()
        return courses
    
    def get_all_exams_for_teacher(self, teacher_id: int):
        courses = self.get_all_courses_for_teacher(teacher_id)
        exams = self.session.query(Exam).filter(Exam.course_id.in_(course.course_id for course in courses)).all()
        return exams
    

    def search_for_student(self, search_query: str):
        students = self.session.query(Student).filter(Student.first_name.ilike(f"%{search_query}%") 
                                                  | Student.user_name.ilike(f"%{search_query}%")
                                                  | Student.last_name.ilike(f"%{search_query}%") 
                                                  | Student.email.ilike(f"%{search_query}%")).all()
        return [student.to_dict() for student in students]
    
    def get_all_active_courses(self, teacher_id: int):
        return self.session.query(Course).filter(Course.teacher_id == teacher_id, Course.is_active == True).all()
    
    def get_all_inactive_courses(self, teacher_id: int):
        return self.session.query(Course).filter(Course.teacher_id == teacher_id, Course.is_active == False).all()
    






    def get_teacher_by_id(self, teacher_id: int):
        return self.session.query(Teacher).filter(Teacher.teacher_id == teacher_id).first()

    def get_all_teachers(self):
        return self.session.query(Teacher).all()

    def create_teacher(self, teacher: Teacher):
        self.session.add(teacher)
        self.session.commit()
        return teacher

    def update_teacher(self, teacher: Teacher):
        self.session.merge(teacher)
        self.session.commit()
        return teacher

    def delete_teacher(self, teacher: Teacher):
        self.session.delete(teacher)
        self.session.commit()
