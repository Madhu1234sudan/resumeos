from pydantic import BaseModel


class ATSRequest(BaseModel):
    jd_text: str


class ATSResponse(BaseModel):
    ats_score: int
    keyword_hit_rate: int
    matched_skills: list[str]
    missing_skills: list[str]
    recommendations: list[str]