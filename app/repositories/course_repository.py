# repositories/course_repository.py

from sqlalchemy.orm import Session

from app.models.course_model import Course
from app.models.enrollment_model import Enrollment
from app.models.student_model import Student
from app.models.exam_model import Exam

class CourseRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_course_by_id(self, course_id: int):
        return self.session.query(Course).filter(Course.id == course_id).first()

    def get_all_courses(self):
        return self.session.query(Course).all()

    def create_course(self, course: Course):
        self.session.add(course)
        self.session.commit()
        return course

    def update_course(self, course: Course):
        self.session.merge(course)
        self.session.commit()
        return course

    def delete_course(self, course: Course):
        self.session.delete(course)
        self.session.commit()

    def get_course_info(self, course_id: int):
        course = self.session.query(Course).filter(Course.course_id == course_id).first()
        enrollments = self.session.query(Enrollment).filter(Enrollment.course_id == course_id).all()
        students = self.session.query(Student).filter(Student.student_id.in_(enrollment.student_id for enrollment in enrollments)).all()
        exams = self.session.query(Exam).filter(Exam.course_id == course_id).all()
        return {
            "course": course.to_dict(),
            "students": [student.to_dict() for student in students],
            "exams": [exam.to_dict() for exam in exams],
        }
    
    def get_exams_for_course(self, course_id: int):
        return self.session.query(Exam).filter(Exam.course_id == course_id).all()

    def get_courses_for_student(self, student_id: int):
        """
        Get all active courses that a student is currently enrolled in.

        Args:
            student_id (int): The ID of the student

        Returns:
            List[Dict]: List of active courses as dictionaries, ordered by course code
        """
        courses = (
            self.session.query(Course)
            .join(Enrollment, Course.course_id == Enrollment.course_id)
            .filter(Enrollment.student_id == student_id, Course.is_active == True)
            .order_by(Course.course_code.asc())
            .all()
        )

        # Use the to_dict() method we defined in the Course model
        return [
            {
                "id": course.course_id,
                "name": course.course_name,
                "code": course.course_code,
                "description": course.course_description,
                "capacity": course.capacity,
            }
            for course in courses
        ]
