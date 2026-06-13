from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.connection import get_db

from middleware.auth_middleware import (
    get_current_user
)

from models.user import User

from schemas.skill import (
    SkillCreateRequest,
    SkillUpdateRequest
)

from services.skill_service import (
    SkillService
)


router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)


@router.post("")
def create_skill(
    request: SkillCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    skill = SkillService.create_skill(
        db,
        current_user,
        request
    )

    return {
        "message": "Skill created successfully",
        "skill_id": skill.id
    }


@router.get("")
def get_skills(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return SkillService.get_skills(
        db,
        current_user
    )


@router.put("/{skill_id}")
def update_skill(
    skill_id: int,
    request: SkillUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    skill = SkillService.update_skill(
        db,
        skill_id,
        current_user,
        request
    )

    if not skill:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    return {
        "message": "Skill updated successfully"
    }


@router.delete("/{skill_id}")
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    deleted = SkillService.delete_skill(
        db,
        skill_id,
        current_user
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Skill not found"
        )

    return {
        "message": "Skill deleted successfully"
    }