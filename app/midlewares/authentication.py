import os
from functools import wraps

import jwt
from flask import jsonify, redirect, request, url_for

from app.database import get_db_session
from app.repositories.student_repository import StudentRepository
from app.services.student_service import StudentService

db_session = get_db_session()
student_repository = StudentRepository(db_session)
student_service = StudentService(student_repository)


# A middleware authentication that verires a jwt before passing request to api routes
def jwt_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        # get jwt from headers passed along with request
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            return jsonify({"error": "No JWT provided"}), 401
        token = token.split(" ")[1]
        try:
            # Verify the JWT token, Clerk using RS256 algo (source from its documentation)
            decoded_token = jwt.decode(
                token, os.getenv("CLERK_JWT_SECRET"), algorithms=["RS256"]
            )
            # Get the Clerk user ID from token
            clerk_user_id = decoded_token["sub"]
        except jwt.InvalidTokenError as e:
            return jsonify({"error": "Invalid JWT token"}), 401

        student = student_service.get_student_by_clerk_id(clerk_user_id)

        if not student or student.clerk_user_id != clerk_user_id:
            return jsonify({"error": "Unauthorized access"}), 401

        return func(*args, **kwargs)

    return wrap
