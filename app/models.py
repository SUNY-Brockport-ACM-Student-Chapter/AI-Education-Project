# Contains all the database models (tables) using SQLAlchemy.

from . import db
from enum import Enum as PyEnum

import uuid
from datetime import datetime


class Role(PyEnum):
    TEACHER = "teacher"
    ADMIN = "admin"


class EnrollmentStatus(PyEnum):
    PENDING = "pending"
    ENROLLED = "enrolled"
    CANCELLED = "cancelled"


class Student(db.Model):
    """
    Represents a user in the system.

    Attributes:
        id (str): The unique identifier for the user.
        user_name (str): The user's username (unique).
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email (unique).
        password_hash (str): The hashed password for the user.
        role (str): The role of the user ('student', 'teacher' or 'admin').
        last_login (DateTime): The last time user logged in.
        created_at (DateTime): when the user account was created.
        updated_at (DateTime): The last time the user’s information was updated.
    """

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self) -> str:
        return f"<Username: {self.user_name}>"


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)
    role = db.Column(db.Enum(Role), nullable=False, default="admin")
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)


class Course(db.Model):
    """
    Represents a course in the system.

    Attributes:
        id (int): The unique identifier for the course.
        course_name (str): The name of the course.
        teacher_id (int): The ID of the teacher for this course.
        teacher (User): The relationship to the User model for the teacher.
    """

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(120), nullable=False)
    course_code = db.Column(db.String(12), nullable=False)
    course_description = db.Column(db.String(255))
    capacity = db.Column(db.Integer, default=10, nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    teacher = db.relationship("Teacher", backref="courses")


class Enrollment(db.Model):
    """
    Represents a course in the system.

    Attributes:
        id (int): The unique identifier for the enrollment.
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.
        status (str) : The status of current enrollment ('enrolled', 'cancelled', 'pending')
        enrollment_date (DateTime): When enrollment was made.
        student (User): The relationship to the User model for the student.
        course (Course): The relationship to the Course model for the course.
    """

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))
    status = db.Column(
        db.Enum(EnrollmentStatus), default=EnrollmentStatus.PENDING, nullable=False
    )
    enrollment_date = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

    student = db.relationship("Student", backref="enrollments")
    course = db.relationship("Course", backref="enrollments")

    def __repr__(self) -> str:
        return f"Enrollment date: {self.enrollment_date}\nStatus: {self.coursestatus}"


class Exam(db.Model):
    """
    Represents an exam in the system.

    Attributes:
        id (int): The unique identifier for the exam.
        course_id (int): The ID of the course this exam belongs to.
        exam_title (str): The title of the exam.
        course (Course): The relationship to the Course model.
    """

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))

    exam_title = db.Column(db.String(120), nullable=False)
    exam_description = db.Column(db.String(255), nullable=True)
    start_date = db.Column(db.DateTime, default=datetime.now)
    end_date = db.Column(db.DateTime, default=datetime.now)
    assessment = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

    course = db.relationship("Course", backref="exams")

    def __repr__(self) -> str:
        return f"<Exam Title: {self.exam_title}>"


class Question(db.Model):
    """
    Represents a question in an exam.

    Attributes:
        id (int): The unique identifier for the question.
        exam_id (int): The ID of the exam this question belongs to.
        question_text (str): The text of the question.
        exam (Exam): The relationship to the Exam model.
    """

    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))
    question_text = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

    course = db.relationship("Course", backref="questions")

    def __repr__(self) -> str:
        return f"<Question: {self.question_text}>"


class Answer(db.Model):
    """
    Represents a student's answer to a question.

    Attributes:
        id (int): The unique identifier for the answer.
        question_id (int): The ID of the question this answer is for.
        student_id (int): The ID of the student who provided this answer.
        answer_text (str): The text of the student's answer.
        question (Question): The relationship to the Question model.
        student (User): The relationship to the User model for the student.
    """

    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    answer_text = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)

    question = db.relationship("Question", backref="answers")

    def __repr__(self) -> str:
        return f"<Answer: {self.answer_text}>"


class StudentAnswer(db.Model):
    """
    Represents an AI-generated evaluation of a student's answer.

    Attributes:
        id (int): The unique identifier for the evaluation.
        answer_id (int): The ID of the answer being evaluated.
        score (int): The score given by the AI (0, 1, or 2).
        feedback (str): The feedback provided by the AI.
        answer (Answer): The relationship to the Answer model.
    """

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    answer_text = db.Column(db.String(255), nullable=True)

    student = db.relationship("Student", backref="student_answers")
    question = db.relationship("Question", backref="student_answers")

    def __repr__(self) -> str:
        return f"<Student Answer: {self.answer_text}>"
