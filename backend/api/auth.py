from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from middleware.auth_middleware import get_current_user
from models.user import User

from database.connection import get_db

from schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from services.auth_service import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register_user(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    try:

        user = AuthService.register_user(
            db=db,
            full_name=request.full_name,
            email=request.email,
            password=request.password,
            phone=request.phone,
            linkedin_url=request.linkedin_url,
            github_url=request.github_url,
            location=request.location
        )

        return {
            "message": "User registered successfully",
            "user_id": user.id
        }

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login")
def login_user(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    try:

        return AuthService.login_user(
            db=db,
            email=request.email,
            password=request.password
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )
@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user)
):

    return {
        "id": current_user.id,
        "full_name": current_user.full_name,
        "email": current_user.email,
        "role": current_user.role,
        "is_verified": current_user.is_verified
    }