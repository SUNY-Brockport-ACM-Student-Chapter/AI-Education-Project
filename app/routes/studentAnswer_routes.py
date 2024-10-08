from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from app.models import StudentAnswer, db

# Create a blueprint for the student answer API
student_answer_bp = Blueprint("student_answer_api", __name__)


@student_answer_bp.route("/student_answers", methods=["POST"])
def create_student_answer():
    data = request.get_json()
    new_student_answer = StudentAnswer(
        student_id=data["student_id"],
        question_id=data["question_id"],
        answer_text=data["answer_text"],
        answer_stage=data["answer_stage"],
    )
    db.session.add(new_student_answer)
    db.session.commit()
    return jsonify({"message": "Student answer created successfully."}), 201


@student_answer_bp.route("/student_answers", methods=["GET"])
def get_student_answers():
    student_answers = StudentAnswer.query.all()
    return (
        jsonify(
            [
                {
                    "student_answer_id": answer.student_answer_id,
                    "student_id": answer.student_id,
                    "question_id": answer.question_id,
                    "answer_text": answer.answer_text,
                    "answer_stage": answer.answer_stage,
                }
                for answer in student_answers
            ]
        ),
        200,
    )


@student_answer_bp.route("/student_answers/<int:student_answer_id>", methods=["GET"])
def get_student_answer(student_answer_id):
    student_answer = StudentAnswer.query.get_or_404(student_answer_id)
    return (
        jsonify(
            {
                "student_answer_id": student_answer.student_answer_id,
                "student_id": student_answer.student_id,
                "question_id": student_answer.question_id,
                "answer_text": student_answer.answer_text,
                "answer_stage": student_answer.answer_stage,
            }
        ),
        200,
    )


@student_answer_bp.route("/student_answers/<int:student_answer_id>", methods=["PUT"])
def update_student_answer(student_answer_id):
    data = request.get_json()
    student_answer = StudentAnswer.query.get_or_404(student_answer_id)

    student_answer.student_id = data.get("student_id", student_answer.student_id)
    student_answer.question_id = data.get("question_id", student_answer.question_id)
    student_answer.answer_text = data.get("answer_text", student_answer.answer_text)
    student_answer.answer_stage = data.get("answer_stage", student_answer.answer_stage)

    db.session.commit()
    return jsonify({"message": "Student answer updated successfully."}), 200


@student_answer_bp.route("/student_answers/<int:student_answer_id>", methods=["DELETE"])
def delete_student_answer(student_answer_id):
    student_answer = StudentAnswer.query.get_or_404(student_answer_id)
    db.session.delete(student_answer)
    db.session.commit()
    return jsonify({"message": "Student answer deleted successfully."}), 204
