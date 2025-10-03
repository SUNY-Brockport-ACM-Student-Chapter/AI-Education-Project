# repositories/answer_repository.py
import uuid
from sqlalchemy.orm import Session
from app.models.submission_answer_model import SubmissionAnswer
from app.models.question_model import Question


class SubmissionAnswerRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_submission_answer(self, submission_id: uuid.UUID, question_id: uuid.UUID, response: str): # Added submission_id, fixed type hint, assumed response is str
        """Creates a new SubmissionAnswer."""
        question = (
            self.session.query(Question)
            .filter(Question.question_id == question_id)
            .first()
        )
        if not question:
            raise ValueError("Question not found")
            
        # The SubmissionAnswer model is missing a FK to Submission! (Need to add submission_id)
        # Assuming SubmissionAnswer will be updated to include a submission_id column
        new_answer = SubmissionAnswer(
            submission_id=submission_id,
            question_id=question_id, 
            response=response
        ) 
        self.session.add(new_answer)
        self.session.commit()
        self.session.refresh(new_answer) # Added refresh
        return new_answer

    def get_answer_by_question_id(self, question_id: uuid.UUID): # Renamed method, fixed type
        """Retrieves a single SubmissionAnswer by question ID."""
        answer = (
            self.session.query(SubmissionAnswer)
            .filter(SubmissionAnswer.question_id == question_id)
            .first()
        )
        if not answer:
            raise ValueError("Answer not found") # Corrected typo
        return answer # Corrected variable name

    def update_answer(self, submission_answer_id: uuid.UUID, data: dict): # Changed PK to submission_answer_id for direct update
        """Updates fields on an existing SubmissionAnswer."""
        answer = (
            self.session.query(SubmissionAnswer)
            .filter(SubmissionAnswer.submission_answer_id == submission_answer_id) # Filter by PK
            .first()
        )
        if not answer:
            raise ValueError("Submission Answer not found") # Corrected error message

        for key, value in data.items():
            if hasattr(answer, key): # Used 'answer' instead of 'user'
                setattr(answer, key, value)
                
        self.session.commit() # Commit the changes
        self.session.refresh(answer)
        return answer