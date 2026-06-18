from pydantic import BaseModel


class RewriteRequest(BaseModel):
    jd_text: str


class RewriteResponse(BaseModel):
    original_summary: str
    rewritten_summary: str
    improvements: list[str]