import os
from datetime import datetime, timezone

from flask import Blueprint, request, jsonify
from svix.webhooks import Webhook, WebhookVerificationError

from app.database import get_db_session
from app.models.student_model import Student
from app.repositories.student_repository import StudentRepository
from app.services.student_service import StudentService

# Create blueprint
webhook_bp = Blueprint('webhook_bp', __name__)

# Initialize service with repository
db_session = get_db_session()
student_repository = StudentRepository(db_session)
student_service = StudentService(student_repository)

@webhook_bp.route('/webhooks/user-created', methods=['POST'])
def handle_user_created():
    """Handle Clerk user.created webhook event"""
    try:
        # Get the webhook signature from headers
        svix_id = request.headers.get('svix-id')
        svix_timestamp = request.headers.get('svix-timestamp')
        svix_signature = request.headers.get('svix-signature')

        if not all([svix_id, svix_timestamp, svix_signature]):
            return jsonify({'error': 'Missing webhook verification headers'}), 400

        # Initialize webhook instance with your signing secret
        wh = Webhook(os.getenv('CLERK_WEBHOOK_SECRET'))

        # Verify webhook signature
        try:
            payload = wh.verify(
                request.get_data().decode('utf-8'),
                {
                    'svix-id': svix_id,
                    'svix-timestamp': svix_timestamp,
                    'svix-signature': svix_signature
                }
            )
        except WebhookVerificationError:
            return jsonify({'error': 'Invalid webhook signature'}), 401

        # Extract user data from payload
        user_data = payload.get('data', {})
        
        # Create new student record
        new_student = Student(
            clerk_user_id=user_data.get('id'),
            email=user_data.get('email_addresses', [{}])[0].get('email_address'),
            user_name=user_data.get('username'),
            first_name=user_data.get('first_name'),
            last_name=user_data.get('last_name'),
            created_at=datetime.now(timezone.utc)
        )

        # Save to database
        student_service.create_student(new_student)

        return jsonify({
            'message': 'User successfully created',
            'user_id': new_student.student_id
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
