# routes/student_routes.py

from flask import Blueprint, jsonify, request
from repositories.student_repository import StudentRepository
from services.student_service import StudentService
from database import SessionLocal

student_bp = Blueprint('student', __name__)

@student_bp.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    session = SessionLocal()
    student_repo = StudentRepository(session)
    student_service = StudentService(student_repo)
    student = student_service.get_student(student_id)
    session.close()

    if student:
        return jsonify({
            'student_id': student.student_id,
            'user_name': student.user_name,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'email': student.email,
            'clerk_user_id': student.clerk_user_id,
            'is_active': student.is_active,
            'last_login': student.last_login,
            'created_at': student.created_at,
            'updated_at': student.updated_at
        })
    return jsonify({'error': 'Student not found'}), 404

@student_bp.route('/students', methods=['GET'])
def get_students():
    session = SessionLocal()
    student_repo = StudentRepository(session)
    student_service = StudentService(student_repo)
    students = student_service.list_students()
    session.close()

    return jsonify([{
        'student_id': student.student_id,
        'user_name': student.user_name,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'email': student.email,
        'clerk_user_id': student.clerk_user_id,
        'is_active': student.is_active,
        'last_login': student.last_login,
        'created_at': student.created_at,
        'updated_at': student.updated_at
    } for student in students])

@student_bp.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    session = SessionLocal()
    student_repo = StudentRepository(session)
    student_service = StudentService(student_repo)
    student = student_service.create_new_student(
        user_name=data['user_name'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        clerk_user_id=data['clerk_user_id']
    )
    session.close()

    return jsonify({
        'student_id': student.student_id,
        'user_name': student.user_name,
        'first_name': student.first_name,
        'last_name': student.last_name,
        'email': student.email,
        'clerk_user_id': student.clerk_user_id,
        'is_active': student.is_active,
        'last_login': student.last_login,
        'created_at': student.created_at,
        'updated_at': student.updated_at
    }), 201

@student_bp.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    session = SessionLocal()
    student_repo = StudentRepository(session)
    student_service = StudentService(student_repo)
    student = student_service.update_existing_student(student_id, **data)
    session.close()

    if student:
        return jsonify({
            'student_id': student.student_id,
            'user_name': student.user_name,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'email': student.email,
            'clerk_user_id': student.clerk_user_id,
            'is_active': student.is_active,
            'last_login': student.last_login,
            'created_at': student.created_at,
            'updated_at': student.updated_at
        })
    return jsonify({'error': 'Student not found'}), 404

@student_bp.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    session = SessionLocal()
    student_repo = StudentRepository(session)
    student_service = StudentService(student_repo)
    deleted_student = student_service.delete_student(student_id)
    session.close()

    if deleted_student:
        return jsonify({'message': 'Student deleted successfully'})
    return jsonify({'error': 'Student not found'}), 404
