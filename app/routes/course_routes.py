from datetime import datetime

from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy

from app.models import Course, db

# Create a blueprint for the course API
course_bp = Blueprint("course_api", __name__)


@course_bp.route("/courses", methods=["POST"])
def create_course():
    data = request.get_json()
    new_course = Course(
        course_id=data["course_id"],
        course_name=data["course_name"],
        course_code=data["course_code"],
        course_description=data.get("course_description"),
        capacity=data["capacity"],
        teacher_id=data["teacher_id"],
        is_active=data.get("is_active", False),
        start_date=data["start_date"],
        end_date=data["end_date"],
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.session.add(new_course)
    db.session.commit()
    return jsonify({"message": "Course created successfully."}), 201


@course_bp.route("/courses", methods=["GET"])
def get_courses():
    courses = Course.query.all()
    return (
        jsonify(
            [
                {
                    "course_id": course.course_id,
                    "course_name": course.course_name,
                    "course_code": course.course_code,
                    "course_description": course.course_description,
                    "capacity": course.capacity,
                    "teacher_id": course.teacher_id,
                    "is_active": course.is_active,
                    "start_date": course.start_date,
                    "end_date": course.end_date,
                    "created_at": course.created_at,
                    "updated_at": course.updated_at,
                }
                for course in courses
            ]
        ),
        200,
    )


@course_bp.route("/courses/<string:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return (
        jsonify(
            {
                "course_id": course.course_id,
                "course_name": course.course_name,
                "course_code": course.course_code,
                "course_description": course.course_description,
                "capacity": course.capacity,
                "teacher_id": course.teacher_id,
                "is_active": course.is_active,
                "start_date": course.start_date,
                "end_date": course.end_date,
                "created_at": course.created_at,
                "updated_at": course.updated_at,
            }
        ),
        200,
    )


@course_bp.route("/courses/<string:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json()
    course = Course.query.get_or_404(course_id)

    course.course_name = data.get("course_name", course.course_name)
    course.course_code = data.get("course_code", course.course_code)
    course.course_description = data.get(
        "course_description", course.course_description
    )
    course.capacity = data.get("capacity", course.capacity)
    course.teacher_id = data.get("teacher_id", course.teacher_id)
    course.is_active = data.get("is_active", course.is_active)
    course.start_date = data.get("start_date", course.start_date)
    course.end_date = data.get("end_date", course.end_date)
    course.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify({"message": "Course updated successfully."}), 200


@course_bp.route("/courses/<string:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    return jsonify({"message": "Course deleted successfully."}), 204
