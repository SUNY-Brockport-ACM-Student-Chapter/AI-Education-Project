from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import Teacher, db

# Create a blueprint for the teacher API
teacher_bp = Blueprint("teacher_api", __name__)


@teacher_bp.route("/teachers", methods=["POST"])
def create_teacher():
    data = request.get_json()
    new_teacher = Teacher(
        user_name=data["user_name"],
        first_name=data["first_name"],
        last_name=data.get("last_name"),
        email=data["email"],
        clerk_user_id=data["clerk_user_id"],
        role=data["role"],
        is_active=data.get("is_active", False),
        last_login=data["last_login"],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({"message": "Teacher created successfully."}), 201


@teacher_bp.route("/teachers", methods=["GET"])
def get_teachers():
    teachers = Teacher.query.all()
    return (
        jsonify(
            [
                {
                    "teacher_id": teacher.teacher_id,
                    "user_name": teacher.user_name,
                    "first_name": teacher.first_name,
                    "last_name": teacher.last_name,
                    "email": teacher.email,
                    "clerk_user_id": teacher.clerk_user_id,
                    "role": teacher.role,
                    "is_active": teacher.is_active,
                    "last_login": teacher.last_login,
                    "created_at": teacher.created_at,
                    "updated_at": teacher.updated_at,
                }
                for teacher in teachers
            ]
        ),
        200,
    )


@teacher_bp.route("/teachers/<int:teacher_id>", methods=["GET"])
def get_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    return (
        jsonify(
            {
                "teacher_id": teacher.teacher_id,
                "user_name": teacher.user_name,
                "first_name": teacher.first_name,
                "last_name": teacher.last_name,
                "email": teacher.email,
                "clerk_user_id": teacher.clerk_user_id,
                "role": teacher.role,
                "is_active": teacher.is_active,
                "last_login": teacher.last_login,
                "created_at": teacher.created_at,
                "updated_at": teacher.updated_at,
            }
        ),
        200,
    )


@teacher_bp.route("/teachers/<int:teacher_id>", methods=["PUT"])
def update_teacher(teacher_id):
    data = request.get_json()
    teacher = Teacher.query.get_or_404(teacher_id)

    teacher.user_name = data.get("user_name", teacher.user_name)
    teacher.first_name = data.get("first_name", teacher.first_name)
    teacher.last_name = data.get("last_name", teacher.last_name)
    teacher.email = data.get("email", teacher.email)
    teacher.clerk_user_id = data.get("clerk_user_id", teacher.clerk_user_id)
    teacher.role = data.get("role", teacher.role)
    teacher.is_active = data.get("is_active", teacher.is_active)
    teacher.last_login = data.get("last_login", teacher.last_login)
    teacher.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify({"message": "Teacher updated successfully."}), 200


@teacher_bp.route("/teachers/<int:teacher_id>", methods=["DELETE"])
def delete_teacher(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    db.session.delete(teacher)
    db.session.commit()
    return jsonify({"message": "Teacher deleted successfully."}), 204
