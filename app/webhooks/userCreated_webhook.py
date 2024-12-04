import os #for environment variables
from datetime import datetime, timezone

from flask import Blueprint, request, jsonify 
from svix.webhooks import Webhook, WebhookVerificationError

from app.database import get_db_session
from app.models.student_model import Student
from app.repositories.student_repository import StudentRepository
from app.services.student_service import StudentService

# Create blueprint, register the webhook route.
webhook_bp = Blueprint('webhook_bp', __name__)

# Initialize service with repository, start the database session.
db_session = get_db_session()
student_repository = StudentRepository(db_session)
student_service = StudentService(student_repository)

#define a post endpoint that listens for the user-created webhook event. 
@webhook_bp.route('/webhooks/user-created', methods=['POST'])
def handle_user_created():
    """process the webhook, verify the signature, extract the user data, and update the student record."""
    try:
        # Get the webhook signature from headers
        #svix headers are required for verifying the webhook signature. 
        svix_id = request.headers.get('svix-id')
        svix_timestamp = request.headers.get('svix-timestamp')
        svix_signature = request.headers.get('svix-signature')


        #check for all the webhook headers, if any are missing, return a 400 error. 
        if not all([svix_id, svix_timestamp, svix_signature]):
            return jsonify({'error': 'Missing webhook verification headers'}), 400

        # Initialize webhook instance with your signing secret
        wh = Webhook(os.getenv('CLERK_WEBHOOK_SECRET'))

        # Verify webhook signature with svix headers. 
        try:
            #decodes the raw payload into a string, verifies the headers, and returns the payload. 
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
        



        #we want to add the clerk user id to the student table. 
        #not create a new student record. 
        # Create new student record
        new_student = Student.clerk_user_id(
            clerk_user_id=user_data.get('id'),
            created_at=datetime.now(timezone.utc)
        )

        # Save to database, update the student record. 
        student_service.update_student(new_student)





        return jsonify({
            'message': 'User successfully created',
            'user_id': new_student.student_id
        }), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    
