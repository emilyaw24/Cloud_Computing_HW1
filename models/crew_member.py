from __future__ import annotations

from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CrewMemberBase(BaseModel):
    movie_id: UUID = Field(
        ...,
        description="ID of the related movie (foreign key to Movie).",
        json_schema_extra={"example": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"},
    )
    name: str = Field(
        ...,
        description="Crew member’s full name.",
        json_schema_extra={"example": "Christopher Nolan"},
    )
    role: str = Field(
        ...,
        description="Role of the crew member in the movie (e.g., Director, Actor, Producer).",
        json_schema_extra={"example": "Director"},
    )
    award: Optional[str] = Field(
        None,
        description="Award received for this role if applicable.",
        json_schema_extra={"example": "Academy Award"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "movie_id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                    "name": "Leonardo DiCaprio",
                    "role": "Actor",
                    "award": "Oscar Nominee",
                }
            ]
        }
    }


class CrewMemberCreate(CrewMemberBase):
    """Creation payload for a Crew Member."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "movie_id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                    "name": "Elliot Page",
                    "role": "Actor",
                    "award": None,
                }
            ]
        }
    }


class CrewMemberUpdate(BaseModel):
    """Partial update for a Crew Member; supply only fields to change."""
    name: Optional[str] = Field(None, json_schema_extra={"example": "Elliot Page"})
    role: Optional[str] = Field(None, json_schema_extra={"example": "Producer"})
    award: Optional[str] = Field(None, json_schema_extra={"example": "Golden Globe"})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"role": "Producer"},
                {"award": "Golden Globe"},
            ]
        }
    }


class CrewMemberRead(CrewMemberBase):
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated CrewMember ID.",
        json_schema_extra={"example": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-02-01T08:00:00Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-02-02T09:30:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "bbbbbbbb-bbbb-4bbb-8bbb-bbbbbbbbbbbb",
                    "movie_id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                    "name": "Leonardo DiCaprio",
                    "role": "Actor",
                    "award": "Oscar Nominee",
                    "created_at": "2025-02-01T08:00:00Z",
                    "updated_at": "2025-02-02T09:30:00Z",
                }
            ]
        }
    }
