# models/file_object_model.py
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.database import Base


section_role_enum = Enum("student", "ta", "teacher", name="section_role_enum")

enrollment_status_enum = Enum("enrolled", "pending", "dropped", "banned", name="enrollment_status_enum")

assessment_type_enum = Enum("assignment", "exam", "quiz", "project", name="assessment_type_enum")

question_kind_enum = Enum("mcq", "multi_select", "true_false", "fib", "short", "long", "code", name="question_kind_enum")

submission_status_enum = Enum("draft", "submitted", "graded", "retracted", name="submission_status_enum")

feedback_channel_enum = Enum("human", "ai", name="feedback_channel_enum")

visibility_enum = Enum("private", "public", name="visibility_enum")