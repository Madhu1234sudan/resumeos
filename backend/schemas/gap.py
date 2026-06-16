from pydantic import BaseModel


class GapAnalysisRequest(BaseModel):
    jd_text: str