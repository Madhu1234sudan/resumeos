from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database.base import Base


class Skill(Base):
    __tablename__ = "skills"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    skill_name: Mapped[str] = mapped_column(
        String(255)
    )

    category: Mapped[str] = mapped_column(
        String(100)
    )

    proficiency_level: Mapped[str] = mapped_column(
        String(50)
    )

    user = relationship(
        "User",
        back_populates="skills"
    )
    projects = relationship(
    "Project",
    secondary="project_skills",
    back_populates="skills"
    )