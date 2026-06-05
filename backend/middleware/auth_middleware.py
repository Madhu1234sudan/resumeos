from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from database.connection import get_db

from core.security import decode_access_token

from repositories.user_repository import UserRepository


security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    try:

        token = credentials.credentials.strip('"')

        print("\nTOKEN RECEIVED:")
        print(token)

        print("\nATTEMPTING TO DECODE...\n")

        payload = decode_access_token(token)

        print("\nPAYLOAD:")
        print(payload)

        email = payload.get("sub")

        if not email:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        user = UserRepository.get_by_email(
            db,
            email
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )

        return user

    except Exception as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )