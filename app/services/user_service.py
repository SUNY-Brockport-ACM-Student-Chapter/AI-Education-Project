# services/user_service.py
# Renamed from student_service.py

# Removed unused json import
from app.repositories.user_repository import UserRepository
from app.models.user_model import User # Assuming User model exists
from typing import Optional, List

# Standardizing resource IDs to string (UUIDs)
ID_TYPE = str


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_user_by_id(self, user_id: ID_TYPE) -> Optional[User]:
        """Retrieves a single user by their ID."""
        return self.user_repo.get_user_by_id(user_id)
        
    def update_user(self, user_id: ID_TYPE, data: dict) -> User:
        """Updates an existing user by their ID."""
        return self.user_repo.update_user(user_id, data)
        
    def delete_user(self, user_id: ID_TYPE) -> bool:
        """Deletes a user by their ID."""
        return self.user_repo.delete_user(user_id)

    def search_for_users(self, data: dict) -> List[User]:
        """
        Searches for users based on criteria in 'data'. 
        Renamed from search_for_students for general user consistency.
        """
        return self.user_repo.search_for_users(data)

    def get_students_for_course(self, course_id: ID_TYPE) -> List[User]:
        """Retrieves all students enrolled in a specific course."""
        return self.user_repo.get_students_for_course(course_id)

    def create_user(self, user_data: dict) -> User:
        """Creates a new user."""
        # Renamed from student_data to user_data for resource consistency.
        return self.user_repo.create_user(user_data)
