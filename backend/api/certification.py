from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from database.connection import get_db

from middleware.auth_middleware import (
    get_current_user
)

from models.user import User

from schemas.certification import (
    CertificationCreateRequest,
    CertificationUpdateRequest
)

from services.certification_service import (
    CertificationService
)


router = APIRouter(
    prefix="/certifications",
    tags=["Certifications"]
)


@router.post("")
def create_certification(
    request: CertificationCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    certification = (
        CertificationService.create_certification(
            db,
            current_user,
            request
        )
    )

    return {
        "message": "Certification created successfully",
        "certification_id": certification.id
    }


@router.get("")
def get_certifications(
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return (
        CertificationService.get_certifications(
            db,
            current_user
        )
    )


@router.put("/{certification_id}")
def update_certification(
    certification_id: int,
    request: CertificationUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    certification = (
        CertificationService.update_certification(
            db,
            certification_id,
            current_user,
            request
        )
    )

    if not certification:
        raise HTTPException(
            status_code=404,
            detail="Certification not found"
        )

    return {
        "message": "Certification updated successfully"
    }


@router.delete("/{certification_id}")
def delete_certification(
    certification_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    deleted = (
        CertificationService.delete_certification(
            db,
            certification_id,
            current_user
        )
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Certification not found"
        )

    return {
        "message": "Certification deleted successfully"
    }