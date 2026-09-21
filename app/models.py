import uuid
from datetime import UTC, datetime

from sqlalchemy import DateTime
from sqlmodel import Field, Relationship, SQLModel


def get_datetime_utc() -> datetime:
    return datetime.now(UTC)


class JobBase(SQLModel):
    site: str = Field(min_length=1, max_length=255)
    title: str = Field(min_length=1, max_length=511)
    company: str = Field(min_length=1, max_length=255)
    city: str | None = Field(min_length=1, max_length=255, default=None)
    state: str | None = Field(min_length=1, max_length=255, default=None)
    job_type: str | None = Field(min_length=1, max_length=127, default=None)
    interval: str | None = Field(min_length=1, max_length=127, default=None)
    min_amount: int | None
    max_amount: int | None
    job_url: str = Field(min_length=127, max_length=1023)
    description: str


class Job(JobBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    valid: int = Field(default=1)
    created_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),
    )
    updated_at: datetime | None = Field(
        default_factory=get_datetime_utc,
        sa_type=DateTime(timezone=True),
    )
