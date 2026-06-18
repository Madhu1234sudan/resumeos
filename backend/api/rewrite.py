from fastapi import APIRouter
from fastapi import Depends

from models.user import User

from middleware.auth_middleware import (
    get_current_user
)

from schemas.rewrite import (
    RewriteRequest
)

from services.resume_rewriter import (
    ResumeRewriter
)


router = APIRouter(
    prefix="/rewrite",
    tags=["Resume Rewriter"]
)


@router.post("/resume")
def rewrite_resume(
    request: RewriteRequest,
    current_user: User = Depends(
        get_current_user
    )
):

    return ResumeRewriter.rewrite(
        current_user,
        request.jd_text
    )