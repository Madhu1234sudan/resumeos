from fastapi import APIRouter
from fastapi import Depends

from middleware.auth_middleware import (
    get_current_user
)

from models.user import User

from schemas.gap import (
    GapAnalysisRequest
)

from services.gap_analysis_service import (
    GapAnalysisService
)


router = APIRouter(
    prefix="/gap",
    tags=["Gap Analyzer"]
)


@router.post("/analyze")
def analyze_gap(
    request: GapAnalysisRequest,
    current_user: User = Depends(
        get_current_user
    )
):

    return GapAnalysisService.analyze(
        current_user,
        request.jd_text
    )