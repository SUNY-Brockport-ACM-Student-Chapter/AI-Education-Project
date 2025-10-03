# repositories/question_repository.py
from sqlalchemy.orm import Session
import uuid
from app.models.assessment_model import Assessment
from app.models.question_model import Question


class QuestionRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_questions_for_assessment(self, assessment_id: uuid.UUID): # Fixed type hint
        assessment = self.session.query(Assessment).filter(Assessment.assessment_id == assessment_id).first()
        if not assessment:
            raise ValueError("Assessment not found")
        return self.session.query(Question).filter(Question.assessment_id == assessment_id).all()

    def get_question_by_id(self, question_id: uuid.UUID): # Fixed type hint
        question = self.session.query(Question).filter(Question.question_id == question_id).first()
        if not question:
            raise ValueError("Question not found")
        return question

    def create_question(self, assessment_id: uuid.UUID, data: dict): # Fixed type hint
        assessment = self.session.query(Assessment).filter(Assessment.assessment_id == assessment_id).first()
        if not assessment:
            raise ValueError("Assessment not found")
            
        # FIX: Changed 'exam_id' to 'assessment_id'
        new_question = Question(assessment_id=assessment_id, **data) 
        self.session.add(new_question)
        self.session.commit()
        self.session.refresh(new_question)
        return new_question

    def update_question_by_id(self, question_id: uuid.UUID, data: dict): # Fixed type hint
        question = self.session.query(Question).filter(Question.question_id == question_id).first()
        if not question:
            raise ValueError("Question not found")
        for key, value in data.items():
            if hasattr(question, key):
                setattr(question, key, value)
                
        # FIX: Changed 'session' to 'self.session'
        self.session.flush() 
        self.session.refresh(question)
        return question