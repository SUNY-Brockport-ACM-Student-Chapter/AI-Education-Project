from datetime import datetime, timezone

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Teacher(Base):
    __tablename__ = "teacher"
    # ... existing Teacher attributes and relationships ...
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    User_name = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    clerk_user_id = Column(String(255), nullable=False)
    role = Column(Enum("admin", "teacher"), default="teacher", nullable=False)
    is_active = Column(Boolean, default=False)


class Student(Base):
    __tablename__ = "student"
    # ... existing Student attributes and relationships ...
    student_id = Column(Integer, primary_key=True, autoincrement=True)
    User_name = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(32), nullable=False)
    last_name = Column(String(32), nullable=True)
    email = Column(String(120), unique=True, nullable=False)
    clerk_user_id = Column(String(255), nullable=False)


class Course(Base):
    __tablename__ = "course"
    # ... existing Course attributes and relationships ...
    course_id = Column(String(8), primary_key=True)
    course_name = Column(String(100), nullable=False)
    course_description = Column(String(255), nullable=False)


class Exam(Base):
    __tablename__ = "exam"
    # ... existing Exam attributes and relationships ...
    exam_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(String(8), ForeignKey("course.course_id"), nullable=False)
    exam_name = Column(String(100), nullable=False)
    exam_description = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)


class Question(Base):
    __tablename__ = "question"
    # ... existing Question attributes and relationships ...
    question_id = Column(Integer, primary_key=True, autoincrement=True)
    exam_id = Column(Integer, ForeignKey("exam.exam_id"), nullable=False)
    question_text = Column(String(255), nullable=False)
    question_type = Column(Enum("multiple_choice", "essay"), nullable=False)


class Answer(Base):
    __tablename__ = "answer"
    # ... existing Answer attributes and relationships ...
    answer_id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(Integer, ForeignKey("question.question_id"), nullable=False)
    answer_text = Column(String(255), nullable=False)
    is_correct = Column(Boolean, default=False)


class StudentAnswer(Base):
    __tablename__ = "student_answer"
    # ... existing StudentAnswer attributes and relationships ...
    student_answer_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student.student_id"), nullable=False)
    exam_id = Column(Integer, ForeignKey("exam.exam_id"), nullable=False)
    question_id = Column(Integer, ForeignKey("question.question_id"), nullable=False)
    answer_id = Column(Integer, ForeignKey("answer.answer_id"), nullable=False)


class AiAssessment(Base):
    __tablename__ = "ai_assessment"
    # ... existing AiAssessment attributes and relationships ...
    ai_assessment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_answer_id = Column(
        Integer, ForeignKey("student_answer.student_answer_id"), nullable=False
    )
    ai_assessment_result = Column(String(255), nullable=False)


class Enrollment(Base):
    __tablename__ = "enrollment"
    # ... existing Enrollment attributes and relationships ...
    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student.student_id"), nullable=False)
    course_id = Column(String(8), ForeignKey("course.course_id"), nullable=False)
    status = Column(Enum("enrolled", "cancelled", "padding"), default="enrolled")
    enrollment_date = Column(DateTime, nullable=False)
