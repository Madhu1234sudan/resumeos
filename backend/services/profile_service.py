from sqlalchemy.orm import Session

from models.user import User

from repositories.user_repository import UserRepository


class ProfileService:

    @staticmethod
    def get_profile(
        current_user: User
    ):

        return {
            "id": current_user.id,
            "full_name": current_user.full_name,
            "email": current_user.email,
            "phone": current_user.phone,
            "linkedin_url": current_user.linkedin_url,
            "github_url": current_user.github_url,
            "location": current_user.location,
            "role": current_user.role,
            "is_verified": current_user.is_verified
        }

    @staticmethod
    def update_profile(
        db: Session,
        current_user: User,
        data
    ):

        current_user.full_name = data.full_name
        current_user.phone = data.phone
        current_user.linkedin_url = data.linkedin_url
        current_user.github_url = data.github_url
        current_user.location = data.location

        UserRepository.update(
            db,
            current_user
        )

        return current_user