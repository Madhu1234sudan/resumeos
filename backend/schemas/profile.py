from pydantic import BaseModel


class ProfileUpdateRequest(BaseModel):

    full_name: str
    phone: str
    linkedin_url: str
    github_url: str
    location: str