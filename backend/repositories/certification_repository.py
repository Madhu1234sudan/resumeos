from sqlalchemy.orm import Session

from models.certification import Certification


class CertificationRepository:

    @staticmethod
    def create(
        db: Session,
        certification: Certification
    ):

        db.add(certification)
        db.commit()
        db.refresh(certification)

        return certification

    @staticmethod
    def get_all_by_user(
        db: Session,
        user_id: int
    ):

        return (
            db.query(Certification)
            .filter(
                Certification.user_id == user_id
            )
            .all()
        )

    @staticmethod
    def get_by_id(
        db: Session,
        certification_id: int
    ):

        return (
            db.query(Certification)
            .filter(
                Certification.id == certification_id
            )
            .first()
        )

    @staticmethod
    def update(
        db: Session,
        certification: Certification
    ):

        db.commit()
        db.refresh(certification)

        return certification

    @staticmethod
    def delete(
        db: Session,
        certification: Certification
    ):

        db.delete(certification)
        db.commit()