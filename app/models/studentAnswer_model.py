
import datetime

from database import Base
from sqlalchemy import Boolean, Column, DateTime, Integer, String

class StudentAnswer(Base):
    __tablename__ ="student answer"

    student_answer_id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey =('students.student_id'), nullable = False)
    question_id = Column(Integer, ForeignKey = ('questions.question_id'), nullable= False)
    answer_text = Column(String(255))
    second_attempt_answer = Column(String(255), default = answer_text)
    answer_grade = Column(String(1), nullable=False)
    second_attempt_grade = Column(String(1), default= answer_grade)
    answer_stage = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<StudentAnswer(student_id = {self.student_id}, question_id = {self.question_id})>"
    