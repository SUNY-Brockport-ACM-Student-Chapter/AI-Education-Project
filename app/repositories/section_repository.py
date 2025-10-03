# repositories/section_repository.py
import uuid
from sqlalchemy.orm import Session
from sqlalchemy import or_

# Import models using snake_case IDs
from app.models.section_model import Section
from app.models.user_model import User
from app.models.course_model import Course # Assuming a Course model exists for section lookups


class SectionRepository:
    """
    Handles database operations related to course Sections.
    """
    def __init__(self, session: Session):
        self.session = session

    def get_section_by_id(self, section_id: uuid) -> Section | None:
        """
        Retrieves a single section by its primary key.
        """
        # PK lookup uses session.get for efficiency
        return self.session.get(Section, section_id)

    def get_sections_for_instructor(self, instructor_user_id: uuid) -> list[Section]:
        """
        Retrieves all sections taught by a specific instructor user.
        """
        # 1. Check if the user exists
        user = self.session.get(User, instructor_user_id)
        if not user:
            raise ValueError("Instructor (User) not found")

        # 2. Find all sections where this user is the instructor
        sections = (
            self.session.query(Section)
            .filter(Section.instructor_id == instructor_user_id)
            .order_by(Section.term, Section.name)
            .all()
        )
        return sections

    def create_section(self, instructor_user_id: uuid, course_id: uuid, data: dict) -> Section:
        """
        Creates a new section associated with a course and instructor.
        """
        # Basic validation (Instructor and Course must exist)
        instructor = self.session.get(User, instructor_user_id)
        if not instructor:
            raise ValueError("Instructor (User) not found")
        
        # Assuming Course model exists and has course_id as PK
        course = self.session.get(Course, course_id) 
        if not course:
            raise ValueError("Course not found")

        # Create the new section record
        new_section = Section(
            instructor_id=instructor_user_id, 
            course_id=course_id, 
            is_active=True, 
            **data
        )
        self.session.add(new_section)
        self.session.commit()
        return new_section

    def update_section(self, section_id: uuid, data: dict) -> Section:
        """
        Updates fields on an existing section.
        """
        section = self.get_section_by_id(section_id)
        if not section:
            raise ValueError("Section not found")
            
        for key, value in data.items():
            # Safely update attributes
            if hasattr(section, key):
                setattr(section, key, value)
                
        session.flush()
        session.refresh(section)
        return section

    def toggle_section_status(self, section_id: uuid) -> Section:
        """
        Flips the is_active status of a section (True -> False or False -> True).
        """
        section = self.get_section_by_id(section_id)
        if not section:
            raise ValueError("Section not found")
            
        # Toggle the boolean value
        section.is_active = not section.is_active
        self.session.commit()
        return section
