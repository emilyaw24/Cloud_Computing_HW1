from __future__ import annotations

from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    code: str = Field(
        ...,
        description="Unique course code (e.g., COMS W4701).",
        json_schema_extra={"example": "COMS W4701"},
    )
    title: str = Field(
        ...,
        description="Full course title.",
        json_schema_extra={"example": "Artificial Intelligence"},
    )
    description: Optional[str] = Field(
        None,
        description="Optional long description of the course.",
        json_schema_extra={"example": "Introduction to modern AI techniques and applications."},
    )
    credits: int = Field(
        ...,
        description="Number of credits awarded for the course.",
        json_schema_extra={"example": 3},
    )
    department: str = Field(
        ...,
        description="Owning department or program.",
        json_schema_extra={"example": "Computer Science"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "COMS W4701",
                    "title": "Artificial Intelligence",
                    "description": "Introduction to modern AI techniques and applications.",
                    "credits": 3,
                    "department": "Computer Science",
                }
            ]
        }
    }


class CourseCreate(CourseBase):
    """Creation payload for a Course."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "code": "HIST W3450",
                    "title": "Modern European History",
                    "description": "Survey of European history from 1789 to the present.",
                    "credits": 4,
                    "department": "History",
                }
            ]
        }
    }


class CourseUpdate(BaseModel):
    """Partial update for a Course; supply only fields to change."""
    title: Optional[str] = Field(None, json_schema_extra={"example": "AI: Principles and Applications"})
    description: Optional[str] = Field(None, json_schema_extra={"example": "Updated course syllabus and focus."})
    credits: Optional[int] = Field(None, json_schema_extra={"example": 4})
    department: Optional[str] = Field(None, json_schema_extra={"example": "Data Science"})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"title": "AI: Principles and Applications"},
                {"credits": 4},
            ]
        }
    }


class CourseRead(CourseBase):
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated persistent Course ID.",
        json_schema_extra={"example": "44444444-4444-4444-8444-444444444444"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-01-15T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-01-16T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "44444444-4444-4444-8444-444444444444",
                    "code": "COMS W4701",
                    "title": "Artificial Intelligence",
                    "description": "Introduction to modern AI techniques and applications.",
                    "credits": 3,
                    "department": "Computer Science",
                    "created_at": "2025-01-15T10:20:30Z",
                    "updated_at": "2025-01-16T12:00:00Z",
                }
            ]
        }
    }
