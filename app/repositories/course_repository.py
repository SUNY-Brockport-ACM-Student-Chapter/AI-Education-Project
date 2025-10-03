# repositories/course_repository.py

import uuid
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.course_model import Course
from app.models.section_model import Section
from app.models.user_model import User


class CourseRepository:
    """
    Repository for Course-related database operations.

    Assumes Course columns: course_id (UUID PK), code (UUID or str), title, description,
    capacity (int), created_by (UUID FK to user.user_id), created_at, updated_at.
    """

    def __init__(self, session: Session):
        self.session = session

    def get_course_by_id(self, course_id: uuid.UUID) -> Optional[Course]:
        """Return a single Course by its UUID, or None if not found."""
        return (
            self.session.query(Course)
            .filter(Course.course_id == course_id)
            .first()
        )

    def get_courses_for_teacher(self, teacher_id: uuid.UUID) -> List[Course]:
        """
        Return all courses created by the given teacher (created_by == teacher_id).
        Ordered by Course.code (fallback to title if code is None).
        """
        # Optional: validate teacher exists
        teacher = (
            self.session.query(User).filter(User.user_id == teacher_id).first()
        )
        if not teacher:
            raise ValueError("Teacher (User) not found")

        # Order by code if available, otherwise by title
        return (
            self.session.query(Course)
            .filter(Course.created_by == teacher_id)
            .order_by(Course.code, Course.title)
            .all()
        )

    def create_course(self, teacher_id: uuid.UUID, course_data: dict) -> Course:
        """
        Create a new Course attributed to teacher_id.
        course_data should contain keys matching Course columns (e.g. code, title, description, capacity).
        """
        teacher = (
            self.session.query(User).filter(User.user_id == teacher_id).first()
        )
        if not teacher:
            raise ValueError("Teacher (User) not found")

        new_course = Course(created_by=teacher_id, **course_data)
        self.session.add(new_course)
        self.session.commit()
        # refresh to populate defaults (timestamps, generated PK, etc.)
        self.session.refresh(new_course)
        return new_course

    def update_course(self, course_id: uuid.UUID, course_data: dict) -> Course:
        """
        Update attributes of an existing Course.
        Only keys present in course_data will be updated.
        """
        course = self.get_course_by_id(course_id)
        if not course:
            raise ValueError("Course not found")

        for key, value in course_data.items():
            # only set attributes that exist on the model
            if hasattr(course, key):
                setattr(course, key, value)
            else:
                # optional: ignore unknown keys or raise; here we ignore silently
                continue

        self.session.commit()
        self.session.refresh(course)
        return course

    def delete_course(self, course_id: uuid.UUID) -> None:
        """Delete a course by its UUID. Commits the transaction."""
        course = self.get_course_by_id(course_id)
        if not course:
            raise ValueError("Course not found")
        self.session.delete(course)
        self.session.commit()

    def get_courses_for_student(self, student_id: uuid.UUID) -> List[Course]:
        """
        Return courses associated with a student by joining Sections.
        Assumes Section has fields: section_id, course_id (FK -> Course.course_id), student_id.
        """
        # Optional: validate student exists
        student = (
            self.session.query(User).filter(User.user_id == student_id).first()
        )
        if not student:
            raise ValueError("Student (User) not found")

        courses = (
            self.session.query(Course)
            .join(Section, Section.course_id == Course.course_id)
            .filter(Section.student_id == student_id)
            .order_by(Course.code, Course.title)
            .all()
        )
        return courses
