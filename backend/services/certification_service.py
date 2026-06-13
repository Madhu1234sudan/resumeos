from sqlalchemy.orm import Session

from models.certification import Certification
from models.user import User

from repositories.certification_repository import (
    CertificationRepository
)


class CertificationService:

    @staticmethod
    def create_certification(
        db: Session,
        current_user: User,
        data
    ):

        certification = Certification(
            user_id=current_user.id,
            certification_name=data.certification_name,
            issuing_organization=data.issuing_organization,
            credential_id=data.credential_id,
            credential_url=data.credential_url
        )

        return CertificationRepository.create(
            db,
            certification
        )

    @staticmethod
    def get_certifications(
        db: Session,
        current_user: User
    ):

        return CertificationRepository.get_all_by_user(
            db,
            current_user.id
        )

    @staticmethod
    def update_certification(
        db: Session,
        certification_id: int,
        current_user: User,
        data
    ):

        certification = CertificationRepository.get_by_id(
            db,
            certification_id
        )

        if not certification:
            return None

        if certification.user_id != current_user.id:
            return None

        certification.certification_name = data.certification_name
        certification.issuing_organization = data.issuing_organization
        certification.credential_id = data.credential_id
        certification.credential_url = data.credential_url

        return CertificationRepository.update(
            db,
            certification
        )

    @staticmethod
    def delete_certification(
        db: Session,
        certification_id: int,
        current_user: User
    ):

        certification = CertificationRepository.get_by_id(
            db,
            certification_id
        )

        if not certification:
            return False

        if certification.user_id != current_user.id:
            return False

        CertificationRepository.delete(
            db,
            certification
        )

        return True