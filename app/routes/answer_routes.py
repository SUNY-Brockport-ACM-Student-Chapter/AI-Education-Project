from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import Answer, db

# Create a blueprint for the answer API
answer_bp = Blueprint("answer_api", __name__)


@answer_bp.route("/answers", methods=["POST"])
def create_answer():
    data = request.get_json()
    new_answer = Answer(
        answer_text=data["answer_text"],
        question_id=data["question_id"],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.session.add(new_answer)
    db.session.commit()
    return jsonify({"message": "Answer created successfully."}), 201


@answer_bp.route("/answers", methods=["GET"])
def get_answers():
    answers = Answer.query.all()
    return (
        jsonify(
            [
                {
                    "answer_id": answer.answer_id,
                    "answer_text": answer.answer_text,
                    "question_id": answer.question_id,
                    "created_at": answer.created_at,
                    "updated_at": answer.updated_at,
                }
                for answer in answers
            ]
        ),
        200,
    )


@answer_bp.route("/answers/<int:answer_id>", methods=["GET"])
def get_answer(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    return (
        jsonify(
            {
                "answer_id": answer.answer_id,
                "answer_text": answer.answer_text,
                "question_id": answer.question_id,
                "created_at": answer.created_at,
                "updated_at": answer.updated_at,
            }
        ),
        200,
    )


@answer_bp.route("/answers/<int:answer_id>", methods=["PUT"])
def update_answer(answer_id):
    data = request.get_json()
    answer = Answer.query.get_or_404(answer_id)

    answer.answer_text = data.get("answer_text", answer.answer_text)
    answer.question_id = data.get("question_id", answer.question_id)
    answer.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify({"message": "Answer updated successfully."}), 200


@answer_bp.route("/answers/<int:answer_id>", methods=["DELETE"])
def delete_answer(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    db.session.delete(answer)
    db.session.commit()
    return jsonify({"message": "Answer deleted successfully."}), 204
