from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import Student, db

# Create a blueprint for the student API
student_bp = Blueprint("student_api", __name__)


@student_bp.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()
    new_student = Student(
        user_name=data["user_name"],
        first_name=data["first_name"],
        last_name=data.get("last_name", None),
        email=data["email"],
        clerk_user_id=data["clerk_user_id"],
        is_active=data.get("is_active", False),
        last_login=data["last_login"],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student created successfully."}), 201


@student_bp.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    return (
        jsonify(
            [
                {
                    "student_id": student.student_id,
                    "user_name": student.user_name,
                    "first_name": student.first_name,
                    "last_name": student.last_name,
                    "email": student.email,
                    "clerk_user_id": student.clerk_user_id,
                    "is_active": student.is_active,
                    "last_login": student.last_login,
                    "created_at": student.created_at,
                    "updated_at": student.updated_at,
                }
                for student in students
            ]
        ),
        200,
    )


@student_bp.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return (
        jsonify(
            {
                "student_id": student.student_id,
                "user_name": student.user_name,
                "first_name": student.first_name,
                "last_name": student.last_name,
                "email": student.email,
                "clerk_user_id": student.clerk_user_id,
                "is_active": student.is_active,
                "last_login": student.last_login,
                "created_at": student.created_at,
                "updated_at": student.updated_at,
            }
        ),
        200,
    )


@student_bp.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    data = request.get_json()
    student = Student.query.get_or_404(student_id)

    student.user_name = data.get("user_name", student.user_name)
    student.first_name = data.get("first_name", student.first_name)
    student.last_name = data.get("last_name", student.last_name)
    student.email = data.get("email", student.email)
    student.clerk_user_id = data.get("clerk_user_id", student.clerk_user_id)
    student.is_active = data.get("is_active", student.is_active)
    student.last_login = data.get("last_login", student.last_login)
    student.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify({"message": "Student updated successfully."}), 200


@student_bp.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully."}), 204
