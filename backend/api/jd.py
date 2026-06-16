from fastapi import APIRouter

from schemas.jd import (
    JDParseRequest
)

from services.jd_analyzer import (
    JDAnalyzer
)


router = APIRouter(
    prefix="/jd",
    tags=["JD Parser"]
)


@router.post("/parse")
def parse_job_description(
    request: JDParseRequest
):

    skills = (
        JDAnalyzer.extract_skills(
            request.jd_text
        )
    )

    return {
        "required_skills": skills
    }