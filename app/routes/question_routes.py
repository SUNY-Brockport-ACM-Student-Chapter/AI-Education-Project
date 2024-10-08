from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import Question, db

# Create a blueprint for the question API
question_bp = Blueprint("question_api", __name__)


@question_bp.route("/questions", methods=["POST"])
def create_question():
    data = request.get_json()
    new_question = Question(
        course_id=data["course_id"],
        question_text=data["question_text"],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.session.add(new_question)
    db.session.commit()
    return jsonify({"message": "Question created successfully."}), 201


@question_bp.route("/questions", methods=["GET"])
def get_questions():
    questions = Question.query.all()
    return (
        jsonify(
            [
                {
                    "question_id": question.question_id,
                    "course_id": question.course_id,
                    "question_text": question.question_text,
                    "created_at": question.created_at,
                    "updated_at": question.updated_at,
                }
                for question in questions
            ]
        ),
        200,
    )


@question_bp.route("/questions/<int:question_id>", methods=["GET"])
def get_question(question_id):
    question = Question.query.get_or_404(question_id)
    return (
        jsonify(
            {
                "question_id": question.question_id,
                "course_id": question.course_id,
                "question_text": question.question_text,
                "created_at": question.created_at,
                "updated_at": question.updated_at,
            }
        ),
        200,
    )


@question_bp.route("/questions/<int:question_id>", methods=["PUT"])
def update_question(question_id):
    data = request.get_json()
    question = Question.query.get_or_404(question_id)

    question.course_id = data.get("course_id", question.course_id)
    question.question_text = data.get("question_text", question.question_text)
    question.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify({"message": "Question updated successfully."}), 200


@question_bp.route("/questions/<int:question_id>", methods=["DELETE"])
def delete_question(question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return jsonify({"message": "Question deleted successfully."}), 204
