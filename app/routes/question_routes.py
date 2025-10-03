"""
This module contains routes for the question model, following the /question RESTful pattern.
"""

from flask import Blueprint, current_app, jsonify, request

from app.database import get_db_session
from app.repositories.question_repository import QuestionRepository
from app.services.question_service import QuestionService

# Create the blueprint with RESTful prefix
question_bp = Blueprint("question_bp", __name__, url_prefix="/question")

# Initialize service with repository
db_session = get_db_session()
question_repository = QuestionRepository(db_session)
question_service = QuestionService(question_repository)


@question_bp.route("/", methods=["POST"])
def create_question():
    """POST /question: Create a new question."""
    try:
        data = request.json
        if not data:
            return jsonify({"error": "Missing JSON data"}), 400
        
        # Assuming the service requires all necessary data from the payload
        question = question_service.create_question_from_payload(data)
        
        return jsonify({"id": question.id, "message": "Question created successfully"}), 201
    except ValueError as e:
        current_app.logger.error(f"Error creating question: {str(e)}")
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        current_app.logger.error(f"Internal error creating question: {str(e)}")
        return jsonify({"error": "Failed to create question"}), 500


@question_bp.route("/<string:question_id>", methods=["GET", "PATCH", "DELETE"])
def handle_question(question_id: str):
    """Handle GET, PATCH, and DELETE operations for a single Question."""
    try:
        if request.method == "GET":
            question = question_service.get_question_by_id(question_id)
            if not question:
                return jsonify({"error": "Question not found"}), 404
            return jsonify(question.to_dict()), 200

        elif request.method == "PATCH":
            data = request.json
            if not data:
                return jsonify({"error": "Missing JSON data for update"}), 400

            question = question_service.update_question(question_id, data)
            return jsonify(question.to_dict()), 200

        elif request.method == "DELETE":
            question_service.delete_question(question_id)
            return "", 204
            
    except ValueError as e:
        current_app.logger.error(f"Error handling question {question_id}: {str(e)}")
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Internal error handling question: {str(e)}")
        return jsonify({"error": "Failed to process question request"}), 500


# Collection filter route: Get all questions for a specific assignment
@question_bp.route("/", methods=["GET"])
def get_questions_filtered():
    """GET /question?assignment_id=...: Get questions filtered by assignment_id."""
    try:
        assignment_id = request.args.get("assignment_id")

        if not assignment_id:
            return jsonify({"error": "Missing required query parameter: assignment_id"}), 400

        # Renamed service method from 'get_questions_for_exam'
        questions = question_service.get_questions_for_assignment(assignment_id)
        questions_dicts = [question.to_dict() for question in questions]
        
        return jsonify({"questions": questions_dicts, "message": "Questions fetched successfully"}), 200
        
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        current_app.logger.error(f"Error fetching questions: {str(e)}")
        return jsonify({"error": "Failed to fetch questions"}), 500
