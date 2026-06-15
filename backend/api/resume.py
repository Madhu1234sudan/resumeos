from fastapi import APIRouter
from fastapi import Depends

from middleware.auth_middleware import (
    get_current_user
)

from models.user import User

from services.resume_service import (
    ResumeService
)


router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.get("")
def get_resume(
    current_user: User = Depends(
        get_current_user
    )
):

    return ResumeService.build_resume(
        current_user
    )