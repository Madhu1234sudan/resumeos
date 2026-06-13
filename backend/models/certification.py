from sqlalchemy import String, ForeignKey

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database.base import Base


class Certification(Base):
    __tablename__ = "certifications"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    certification_name: Mapped[str] = mapped_column(
        String(255)
    )

    issuing_organization: Mapped[str] = mapped_column(
        String(255)
    )

    credential_id: Mapped[str] = mapped_column(
        String(255)
    )

    credential_url: Mapped[str] = mapped_column(
        String(500)
    )

    user = relationship(
        "User",
        back_populates="certifications"
    )