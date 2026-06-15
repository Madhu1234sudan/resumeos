from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from database.connection import get_db

from middleware.auth_middleware import (
    get_current_user
)

from models.user import User

from schemas.profile import (
    ProfileUpdateRequest
)

from services.profile_service import (
    ProfileService
)

from services.profile_summary_service import (
    ProfileSummaryService
)


router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("")
def get_profile(
    current_user: User = Depends(
        get_current_user
    )
):

    return ProfileService.get_profile(
        current_user
    )


@router.get("/summary")
def get_profile_summary(
    current_user: User = Depends(
        get_current_user
    )
):

    return (
        ProfileSummaryService.generate_summary(
            current_user
        )
    )


@router.put("")
def update_profile(
    request: ProfileUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    updated_user = (
        ProfileService.update_profile(
            db,
            current_user,
            request
        )
    )

    return {
        "message": "Profile updated successfully",
        "user_id": updated_user.id
    }