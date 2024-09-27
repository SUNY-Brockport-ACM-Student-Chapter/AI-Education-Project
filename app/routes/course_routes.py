"""
This module contains routes and functions related to course management in the application.

It defines a Flask Blueprint for course-related routes and includes functions for
handling course operations such as listing courses, creating courses, and managing
course details.
"""

from flask import Blueprint, jsonify, current_app

# Create a Blueprint named 'course_bp'
course_bp = Blueprint('course_bp', __name__)
 
# API endpoint: create a course
@course_bp.route('/courses', methods=['POST'])
def create_course():
    return jsonify({"message": "create a course"}), 400
    

# API endpoint: get all courses
@course_bp.route('/courses', methods=['GET'])
def list_courses():
    return jsonify({"message": "get all course"}), 404
   
# API endpoint: get a specific course.
@course_bp.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return jsonify({"message": "get a specific course"}), 404
    
# API endpoint: update a specific course
@course_bp.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    return jsonify({"message": "update a specific course"}), 404
    

# API endpoint: update a specific course
@course_bp.route('/courses/<int:course_id>', methods=['DELETE']) 
def delete_course(course_id):
    return jsonify({"message": "delete a specific course"}), 400
    

