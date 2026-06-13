from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.connection import get_db

from middleware.auth_middleware import (
    get_current_user
)

from models.user import User

from schemas.project import (
    ProjectCreateRequest,
    ProjectUpdateRequest
)

from services.project_service import (
    ProjectService
)


router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)


@router.post("")
def create_project(
    request: ProjectCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    project = ProjectService.create_project(
        db,
        current_user,
        request
    )

    return {
        "message": "Project created successfully",
        "project_id": project.id
    }


@router.get("")
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return ProjectService.get_projects(
        db,
        current_user
    )


@router.put("/{project_id}")
def update_project(
    project_id: int,
    request: ProjectUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    project = ProjectService.update_project(
        db,
        project_id,
        current_user,
        request
    )

    if not project:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project updated successfully"
    }


@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    deleted = ProjectService.delete_project(
        db,
        project_id,
        current_user
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Project not found"
        )

    return {
        "message": "Project deleted successfully"
    }