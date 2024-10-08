from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import Enrollment, db

# Create a blueprint for the enrollment API
enrollment_bp = Blueprint("enrollment_api", __name__)


@enrollment_bp.route("/enrollments", methods=["POST"])
def create_enrollment():
    data = request.get_json()
    new_enrollment = Enrollment(
        student_id=data["student_id"],
        course_id=data["course_id"],
        status=data.get("status", "enrolled"),
        enrollment_date=datetime.utcnow(),
    )
    db.session.add(new_enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment created successfully."}), 201


@enrollment_bp.route("/enrollments", methods=["GET"])
def get_enrollments():
    enrollments = Enrollment.query.all()
    return (
        jsonify(
            [
                {
                    "enrollment_id": enrollment.enrollment_id,
                    "student_id": enrollment.student_id,
                    "course_id": enrollment.course_id,
                    "status": enrollment.status,
                    "enrollment_date": enrollment.enrollment_date,
                }
                for enrollment in enrollments
            ]
        ),
        200,
    )


@enrollment_bp.route("/enrollments/<int:enrollment_id>", methods=["GET"])
def get_enrollment(enrollment_id):
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    return (
        jsonify(
            {
                "enrollment_id": enrollment.enrollment_id,
                "student_id": enrollment.student_id,
                "course_id": enrollment.course_id,
                "status": enrollment.status,
                "enrollment_date": enrollment.enrollment_date,
            }
        ),
        200,
    )


@enrollment_bp.route("/enrollments/<int:enrollment_id>", methods=["PUT"])
def update_enrollment(enrollment_id):
    data = request.get_json()
    enrollment = Enrollment.query.get_or_404(enrollment_id)

    enrollment.student_id = data.get("student_id", enrollment.student_id)
    enrollment.course_id = data.get("course_id", enrollment.course_id)
    enrollment.status = data.get("status", enrollment.status)
    enrollment.enrollment_date = data.get("enrollment_date", enrollment.enrollment_date)

    db.session.commit()
    return jsonify({"message": "Enrollment updated successfully."}), 200


@enrollment_bp.route("/enrollments/<int:enrollment_id>", methods=["DELETE"])
def delete_enrollment(enrollment_id):
    enrollment = Enrollment.query.get_or_404(enrollment_id)
    db.session.delete(enrollment)
    db.session.commit()
    return jsonify({"message": "Enrollment deleted successfully."}), 204
