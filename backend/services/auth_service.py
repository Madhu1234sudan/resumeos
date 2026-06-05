from sqlalchemy.orm import Session

from models.user import User
from repositories.user_repository import UserRepository
from core.security import hash_password

from core.security import (
    verify_password,
    create_access_token
)

class AuthService:

    @staticmethod
    def register_user(
        db: Session,
        full_name: str,
        email: str,
        password: str,
        phone: str = "",
        linkedin_url: str = "",
        github_url: str = "",
        location: str = ""
    ):

        existing_user = (
            UserRepository.get_by_email(
                db,
                email
            )
        )

        if existing_user:
            raise ValueError(
                "User already exists"
            )

        user = User(
            full_name=full_name,
            email=email,
            password_hash=hash_password(
                password
            ),
            phone=phone,
            linkedin_url=linkedin_url,
            github_url=github_url,
            location=location
        )

        return UserRepository.create(
            db,
            user
        )
    @staticmethod
    def login_user(
        db: Session,
            email: str,
            password: str
        ):

            user = UserRepository.get_by_email(
                db,
                email
            )

            if not user:
                raise ValueError(
                    "Invalid credentials"
                )

            if not verify_password(
                password,
                user.password_hash
            ):
                raise ValueError(
                    "Invalid credentials"
                )

            token = create_access_token(
                {
                    "sub": user.email,
                    "role": user.role
                }
            )

            return {
                "access_token": token,
                "token_type": "bearer"
            }   