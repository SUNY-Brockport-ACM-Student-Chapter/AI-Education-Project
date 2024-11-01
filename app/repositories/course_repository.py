# repositories/course_repository.py

from sqlalchemy.orm import Session

from app.models.course_model import Course
from app.models.enrollment_model import Enrollment


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

    def get_courses_for_student(self, student_id: int):
        """
        Get all active courses that a student is currently enrolled in.
        
        Args:
            student_id (int): The ID of the student
            
        Returns:
            List[Course]: List of active courses ordered by course code
        """
        return (
            self.session.query(Course)
            .join(Enrollment, Course.course_id == Enrollment.course_id)
            .filter(
                Enrollment.student_id == student_id,
                Course.is_active == True
            )
            .order_by(Course.course_code.asc())
            .all()
        )
