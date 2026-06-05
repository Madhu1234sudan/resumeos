
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.base import Base
from sqlalchemy import (
    String,
    Boolean,
    DateTime
)

from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    full_name: Mapped[str] = mapped_column(
        String(255)
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True
    )

    phone: Mapped[str] = mapped_column(
        String(50)
    )

    linkedin_url: Mapped[str] = mapped_column(
        String(500)
    )

    github_url: Mapped[str] = mapped_column(
        String(500)
    )

    location: Mapped[str] = mapped_column(
        String(255)
    )

    skills = relationship(
        "Skill",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    projects = relationship(
    "Project",
    back_populates="user",
    cascade="all, delete-orphan"
    )
    password_hash: Mapped[str] = mapped_column(
    String(255)
    )

    role: Mapped[str] = mapped_column(
        String(50),
        default="user"
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    