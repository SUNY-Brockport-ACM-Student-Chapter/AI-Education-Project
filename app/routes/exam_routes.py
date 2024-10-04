from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app.models import Exam,db


# Create a blueprint for the exam API
exam_bp = Blueprint('exam_api', __name__)

@exam_bp.route('/exams', methods=['POST'])
def create_exam():
    data = request.get_json()
    new_exam = Exam(
        course_id=data['course_id'],
        exam_name=data['exam_name'],
        exam_description=data.get('exam_description', None),
        start_date=data['start_date'],
        end_date=data['end_date'],
        assessment=data.get('assessment', None),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    db.session.add(new_exam)
    db.session.commit()
    return jsonify({'message': 'Exam created successfully.'}), 201

@exam_bp.route('/exams', methods=['GET'])
def get_exams():
    exams = Exam.query.all()
    return jsonify([{
        'exam_id': exam.exam_id,
        'course_id': exam.course_id,
        'exam_name': exam.exam_name,
        'exam_description': exam.exam_description,
        'start_date': exam.start_date,
        'end_date': exam.end_date,
        'assessment': exam.assessment,
        'created_at': exam.created_at,
        'updated_at': exam.updated_at
    } for exam in exams]), 200

@exam_bp.route('/exams/<int:exam_id>', methods=['GET'])
def get_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    return jsonify({
        'exam_id': exam.exam_id,
        'course_id': exam.course_id,
        'exam_name': exam.exam_name,
        'exam_description': exam.exam_description,
        'start_date': exam.start_date,
        'end_date': exam.end_date,
        'assessment': exam.assessment,
        'created_at': exam.created_at,
        'updated_at': exam.updated_at
    }), 200

@exam_bp.route('/exams/<int:exam_id>', methods=['PUT'])
def update_exam(exam_id):
    data = request.get_json()
    exam = Exam.query.get_or_404(exam_id)

    exam.course_id = data.get('course_id', exam.course_id)
    exam.exam_name = data.get('exam_name', exam.exam_name)
    exam.exam_description = data.get('exam_description', exam.exam_description)
    exam.start_date = data.get('start_date', exam.start_date)
    exam.end_date = data.get('end_date', exam.end_date)
    exam.assessment = data.get('assessment', exam.assessment)
    exam.updated_at = datetime.utcnow()

    db.session.commit()
    return jsonify({'message': 'Exam updated successfully.'}), 200

@exam_bp.route('/exams/<int:exam_id>', methods=['DELETE'])
def delete_exam(exam_id):
    exam = Exam.query.get_or_404(exam_id)
    db.session.delete(exam)
    db.session.commit()
    return jsonify({'message': 'Exam deleted successfully.'}), 204
