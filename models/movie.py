from __future__ import annotations

from uuid import UUID, uuid4
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class MovieBase(BaseModel):
    title: str = Field(
        ...,
        description="Movie title.",
        json_schema_extra={"example": "Inception"},
    )
    genre: str = Field(
        ...,
        description="Movie genre.",
        json_schema_extra={"example": "Science Fiction"},
    )
    release_year: int = Field(
        ...,
        description="Year the movie was released.",
        json_schema_extra={"example": 2010},
    )
    description: Optional[str] = Field(
        None,
        description="Optional synopsis or description of the movie.",
        json_schema_extra={
            "example": "PLOT OF INCEPTION HERE."
        },
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Inception",
                    "genre": "Science Fiction",
                    "release_year": 2010,
                    "description": "PLOT OF INCEPTION HERE.",
                }
            ]
        }
    }


class MovieCreate(MovieBase):
    """Creation payload for a Movie."""
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Blade Runner 2049",
                    "genre": "Science Fiction",
                    "release_year": 2017,
                    "description": "PLOT OF BLADE RUNNER HERE.",
                }
            ]
        }
    }


class MovieUpdate(BaseModel):
    """Partial update for a Movie; supply only fields to change."""
    title: Optional[str] = Field(None, json_schema_extra={"example": "Inception (Director's Cut)"})
    genre: Optional[str] = Field(None, json_schema_extra={"example": "Thriller"})
    release_year: Optional[int] = Field(None, json_schema_extra={"example": 2011})
    description: Optional[str] = Field(None, json_schema_extra={"example": "Extended edition with new scenes."})

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"title": "Inception (Director's Cut)"},
                {"release_year": 2011},
                {"description": "Extended edition with new scenes."},
            ]
        }
    }


class MovieRead(MovieBase):
    id: UUID = Field(
        default_factory=uuid4,
        description="Server-generated persistent Movie ID.",
        json_schema_extra={"example": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa"},
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Creation timestamp (UTC).",
        json_schema_extra={"example": "2025-02-01T10:20:30Z"},
    )
    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="Last update timestamp (UTC).",
        json_schema_extra={"example": "2025-02-02T12:00:00Z"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "aaaaaaaa-aaaa-4aaa-8aaa-aaaaaaaaaaaa",
                    "title": "Inception",
                    "genre": "Science Fiction",
                    "release_year": 2010,
                    "description": "PLOT OF INCEPTION HERE.",
                    "created_at": "2025-02-01T10:20:30Z",
                    "updated_at": "2025-02-02T12:00:00Z",
                }
            ]
        }
    }
