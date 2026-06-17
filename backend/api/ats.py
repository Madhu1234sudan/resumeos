from fastapi import APIRouter
from fastapi import Depends

from models.user import User

from middleware.auth_middleware import (
    get_current_user
)

from schemas.ats import (
    ATSRequest
)

from services.ats_scorer import (
    ATSScorer
)


router = APIRouter(
    prefix="/ats",
    tags=["ATS Scorer"]
)


@router.post("/score")
def score_resume(
    request: ATSRequest,
    current_user: User = Depends(
        get_current_user
    )
):

    return ATSScorer.score(
        current_user,
        request.jd_text
    )