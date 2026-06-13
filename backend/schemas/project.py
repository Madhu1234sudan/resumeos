from pydantic import BaseModel


class ProjectCreateRequest(BaseModel):

    project_name: str
    description: str
    github_url: str


class ProjectUpdateRequest(BaseModel):

    project_name: str
    description: str
    github_url: str