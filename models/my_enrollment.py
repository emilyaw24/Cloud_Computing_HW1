from __future__ import annotations

from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class EnrollmentBase(BaseModel):
    person_id: UUID = Field(
        ...,
        description="ID of the enrolled person (foreign key to Person).",
        json_schema_extra={"example": "99999999-9999-4999-8999-999999999999"},
    )
    course_id: UUID = Field(
        ...,
        description="ID of the course (foreign key to Course).",
        json_schema_extra={"example": "44444444-4444-4444-8444-444444444444"},
    )
    role: str = Field(
        default="student",
        description="Role of the person in the course (e.g., student, instructor, TA).",
        json_schema_extra={"example": "student"},
    )
    grade: Optional[str] = Field(
        None,
        description="Final letter grade if applicable.",
        json_schema_extra={"example": "A"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "person_id": "99999999-9999-4999-8999-999999999999",
                    "course_id": "44444444-4444-4444-8444-444444444444",
                    "role": "student",
                    "grade": "A",
                }
            ]
        }
    }


class EnrollmentCreate(EnrollmentBase):
    """Creation payload for an Enrollment."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "person_id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                    "course_id": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb",
                    "role": "instructor",
                }
            ]
        }
    }


class EnrollmentUpdate(BaseModel):
    """Partial update for an Enrollment; supply only fields to change."""
    role: Optional[str] = Field(None, json_schema_extra={"example": "TA"})
    grade: Optional[str] = Field(None, json_schema_extra={"example": "B+"})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"role": "TA"},
                {"grade": "A-"},
            ]
        }
    }


class EnrollmentRead(EnrollmentBase):
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated Enrollment ID.",
        json_schema_extra={"example": "77777777-7777-4777-8777-777777777777"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-20T08:00:00Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-21T09:30:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "77777777-7777-4777-8777-777777777777",
                    "person_id": "99999999-9999-4999-8999-999999999999",
                    "course_id": "44444444-4444-4444-8444-444444444444",
                    "role": "student",
                    "grade": "A",
                    "created_at": "2025-01-20T08:00:00Z",
                    "updated_at": "2025-01-21T09:30:00Z",
                }
            ]
        }
    }
