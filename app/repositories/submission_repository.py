# repositories/submission_repository.py

import uuid
from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.submission_model import Submission
from app.models.user_model import User
from app.models.assessment_model import Assessment


class SubmissionRepository:
    """
    Repository for Submission-related DB operations.

    Assumes:
    - Submission.submission_id is UUID PK (no DB default)
    - Assessment and User models exist and use user_id and assessment_id UUID PKs.
    """

    def __init__(self, session: Session):
        self.session = session

    def get_submission_by_id(self, submission_id: uuid.UUID) -> Optional[Submission]:
        """Return a Submission by its UUID or None if not found."""
        return (
            self.session.query(Submission)
            .filter(Submission.submission_id == submission_id)
            .first()
        )

    def list_for_assessment(self, assessment_id: uuid.UUID) -> List[Submission]:
        """Return all (non-deleted) submissions for an assessment ordered by attempt_number."""
        return (
            self.session.query(Submission)
            .filter(
                Submission.assessment_id == assessment_id,
                Submission.deleted_at.is_(None),
            )
            .order_by(Submission.attempt_number.asc(), Submission.submitted_at.asc())
            .all()
        )

    def list_for_user(self, user_id: uuid.UUID) -> List[Submission]:
        """Return all (non-deleted) submissions for a given user."""
        return (
            self.session.query(Submission)
            .filter(Submission.user_id == user_id, Submission.deleted_at.is_(None))
            .order_by(Submission.created_at.desc())
            .all()
        )

    def get_latest_attempt(self, user_id: uuid.UUID, assessment_id: uuid.UUID) -> Optional[Submission]:
        """
        Return the latest attempt (highest attempt_number) for a user on a given assessment.
        Returns None if no attempts exist.
        """
        return (
            self.session.query(Submission)
            .filter(
                Submission.user_id == user_id,
                Submission.assessment_id == assessment_id,
                Submission.deleted_at.is_(None),
            )
            .order_by(Submission.attempt_number.desc(), Submission.submitted_at.desc())
            .first()
        )

    def create_submission(self, assessment_id: uuid.UUID, user_id: uuid.UUID, *,
                          attempt_number: Optional[int] = None,
                          status: str = "submitted",
                          submitted_at: Optional[datetime] = None,
                          **extra_fields) -> Submission:
        """
        Create a new Submission. If attempt_number is omitted, it will calculate
        the next attempt number for this user+assessment.
        extra_fields may include score, late_penalty, final, grader_id, etc.
        """
        # validate user and assessment exist
        user = self.session.query(User).filter(User.user_id == user_id).first()
        if not user:
            raise ValueError("User not found")

        assessment = (
            self.session.query(Assessment)
            .filter(Assessment.assessment_id == assessment_id)
            .first()
        )
        if not assessment:
            raise ValueError("Assessment not found")

        # determine attempt_number if not provided
        if attempt_number is None:
            last = self.get_latest_attempt(user_id, assessment_id)
            attempt_number = 1 if last is None else (last.attempt_number + 1)

        sub_id = uuid.uuid4()
        now = datetime.now(timezone.utc)
        if submitted_at is None and status == "submitted":
            submitted_at = now

        new_submission = Submission(
            submission_id=sub_id,
            assessment_id=assessment_id,
            user_id=user_id,
            attempt_number=attempt_number,
            status=status,
            submitted_at=submitted_at,
            created_at=now,
            updated_at=now,
            **extra_fields,
        )

        self.session.add(new_submission)
        self.session.commit()
        self.session.refresh(new_submission)
        return new_submission

    def update_submission(self, submission_id: uuid.UUID, updates: dict) -> Submission:
        """
        Update allowed fields on a submission.
        Ignores unknown attributes to avoid accidental writes.
        """
        submission = self.get_by_id(submission_id)
        if not submission:
            raise ValueError("Submission not found")

        # Allowed fields to update (you can expand this list if needed)
        allowed = {
            "attempt_number",
            "status",
            "submitted_at",
            "graded_at",
            "grader_id",
            "score",
            "late_penalty",
            "final",
            "deleted_at",
        }

        changed = False
        for key, value in updates.items():
            if key in allowed and hasattr(submission, key):
                setattr(submission, key, value)
                changed = True

        if changed:
            # updated_at will be set by SQLAlchemy `onupdate` if configured; set fallback
            submission.updated_at = datetime.now(timezone.utc)
            self.session.commit()
            self.session.refresh(submission)

        return submission

        return self.update_submission(submission_id, {"status": status})

    def soft_delete(self, submission_id: uuid.UUID, deleted_at: Optional[datetime] = None) -> Submission:
        """
        Soft-delete a submission by setting deleted_at to now (or provided datetime).
        """
        submission = self.get_by_id(submission_id)
        if not submission:
            raise ValueError("Submission not found")

        deleted_at = deleted_at or datetime.now(timezone.utc)
        return self.update_submission(submission_id, {"deleted_at": deleted_at})

    def hard_delete(self, submission_id: uuid.UUID) -> None:
        """Permanently remove submission from DB."""
        submission = self.get_by_id(submission_id)
        if not submission:
            raise ValueError("Submission not found")
        self.session.delete(submission)
        self.session.commit()
