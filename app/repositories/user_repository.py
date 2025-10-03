import json
import uuid
from sqlalchemy.orm import Session
from app.models.section_model import Section
from app.models.user_model import User  


class UserRepository: 
    """
    The Repository layer component responsible for handling all database 
    interactions (CRUD operations) for the User entity.
    """
    def __init__(self, session: Session):
        self.session = session

    def search_for_users(self, data: dict): 
        """
        Searches for User records based on provided criteria (user_name, first_name, last_name, email).
        """
        if not data:
            raise ValueError("Search query is required")
        search_query = ""
        if data.get("user_name"):
            search_query += data.get("user_name")
        if data.get("first_name"):
            search_query += data.get("first_name")
        if data.get("last_name"):
            search_query += data.get("last_name")
        if data.get("email"):
            search_query += data.get("email")
            
        users = (  # Changed variable name
            self.session.query(User)  # Changed model reference
            .filter(
                User.user_name.ilike(f"%{search_query}%") 
                | User.first_name.ilike(f"%{search_query}%") 
                | User.last_name.ilike(f"%{search_query}%") 
                | User.email.ilike(f"%{search_query}%") 
            )
            .all()
        )
        if not users:
            raise ValueError("No users found") 
        return users

    def get_users_for_section(self, section_id: uuid): 
        """
        Retrieves all users enrolled in a specific section.
        """
        sections = (
            self.session.query(Section)
            .filter(Section.section_id == section_id)
            .all()
        )
        
        # Assume enrollment.user is the relationship property now.
        users = [section.user for section in sections]
        
        # Deduplicate the list of users efficiently
        unique_users = list(set(users))
        
        if not unique_users:
            raise ValueError("No users found")  
            
        return unique_users

    def create_user(self, user_data: json): 
        """
        Placeholder for creating a new user record. 
        """
        return user_data  

    def get_user_by_id(self, user_id: uuid):
        """Get a teacher by their ID"""
        user = (
            self.session.query(User).filter(User.user_id == user_id).first()
        )
        if not user:
            raise ValueError("Teacher not found")
        return user

    def update_user_by_id(self,user_id, user_data: dict):
        # 1. Fetch the user object
        user = session.get(User, user_id)
        
        if user:
            # 2. Update attributes based on input data
            for key, value in data.items():
                # Safely update only the attributes provided
                if hasattr(user, key):
                    setattr(user, key, value)

            # 3. Flush to execute the UPDATE statement and trigger the 'onupdate' for 'updated_at'
            session.flush()
            # 4. Refresh to load the newly generated 'updated_at' value into the object
            session.refresh(user)

