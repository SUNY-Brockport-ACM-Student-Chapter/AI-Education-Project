from flask import Blueprint, jsonify, request, current_app
from datetime import datetime, timezone
from clerk import Clerk
import os

from app.database import get_db_session
from app.models.student_model import Student
from app.repositories.student_repository import StudentRepository
from app.services.student_service import StudentService

student_auth_bp = Blueprint("student_auth_bp", __name__)

# Initialize Clerk
clerk = Clerk(secret_key=os.getenv('CLERK_SECRET_KEY'))

# Initialize service with repository
db_session = get_db_session()
student_repository = StudentRepository(db_session)
student_service = StudentService(student_repository)

@student_auth_bp.route("/login", methods=["POST"])
def login():
    """Student login endpoint with Clerk authentication"""
    try:
        # Get the session token from the Authorization header
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "No authorization token provided"}), 401

        session_token = auth_header.split(' ')[1]

        try:
            # Verify the session with Clerk
            session_claims = clerk.sessions.verify_session(session_token)
            clerk_user_id = session_claims['sub']  # Get the Clerk user ID
        except Exception as e:
            current_app.logger.error(f"Clerk verification failed: {str(e)}")
            return jsonify({"error": "Invalid authentication token"}), 401

        # Get student by Clerk user ID
        student = student_service.get_student_by_clerk_id(clerk_user_id)
        
        if not student:
            return jsonify({"error": "Student account not found"}), 404

        # Update last login time
        student.last_login = datetime.now(timezone.utc)
        student_service.update_student(student)

        return jsonify({
            "message": "Login successful",
            "student": {
                "student_id": student.student_id,
                "username": student.user_name,
                "email": student.email,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "clerk_user_id": student.clerk_user_id
            }
        }), 200

    except Exception as e:
        current_app.logger.error(f"Login error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

@student_auth_bp.route("/clerk-webhook", methods=["POST"])
def clerk_webhook():
    """Handle Clerk webhooks for user creation/updates"""
    try:
        # Verify webhook signature
        svix_id = request.headers.get("svix-id")
        svix_timestamp = request.headers.get("svix-timestamp")
        svix_signature = request.headers.get("svix-signature")

        if not all([svix_id, svix_timestamp, svix_signature]):
            return jsonify({"error": "Missing webhook verification headers"}), 400

        # Get the webhook body
        webhook_data = request.json
        event_type = webhook_data.get("type")
        
        if event_type == "user.created":
            # Handle new user creation
            user_data = webhook_data.get("data", {})
            email = user_data.get("email_addresses", [{}])[0].get("email_address")
            first_name = user_data.get("first_name", "")
            last_name = user_data.get("last_name", "")
            clerk_user_id = user_data.get("id")

            # Create new student
            new_student = Student(
                email=email,
                first_name=first_name,
                last_name=last_name,
                clerk_user_id=clerk_user_id,
                user_name=email  # You might want to generate a username differently
            )
            student_service.create_student(new_student)

        return jsonify({"message": "Webhook processed successfully"}), 200

    except Exception as e:
        current_app.logger.error(f"Webhook error: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500
