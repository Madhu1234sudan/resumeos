from models.project_skill import ProjectSkill
from sqlalchemy import String, ForeignKey, Text
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    project_name: Mapped[str] = mapped_column(
        String(255)
    )

    description: Mapped[str] = mapped_column(
        Text
    )

    github_url: Mapped[str] = mapped_column(
        String(500)
    )

    user = relationship(
        "User",
        back_populates="projects"
    )
    skills = relationship(
    "Skill",
    secondary="project_skills",
    back_populates="projects"
    )