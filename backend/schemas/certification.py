from pydantic import BaseModel


class CertificationCreateRequest(BaseModel):

    certification_name: str
    issuing_organization: str
    credential_id: str
    credential_url: str


class CertificationUpdateRequest(BaseModel):

    certification_name: str
    issuing_organization: str
    credential_id: str
    credential_url: str