from pydantic import BaseModel


class JDParseRequest(BaseModel):
    jd_text: str


class JDParseResponse(BaseModel):
    required_skills: list[str]