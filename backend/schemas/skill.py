from pydantic import BaseModel


class SkillCreateRequest(BaseModel):

    skill_name: str
    category: str
    proficiency_level: str


class SkillUpdateRequest(BaseModel):

    skill_name: str
    category: str
    proficiency_level: str