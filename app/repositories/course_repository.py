# repositories/course_repository.py

from sqlalchemy.orm import Session

from models import Course


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
