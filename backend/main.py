from fastapi import FastAPI

from api.auth import router as auth_router
from api.profile import router as profile_router
from api.skill import router as skill_router
from api.project import router as project_router
from api.certification import router as certification_router
from api.resume import (
    router as resume_router
)



app = FastAPI(
    title="ResumeOS API",
    version="1.0.0"
)


app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(skill_router)
app.include_router(project_router)
app.include_router(certification_router)
app.include_router(resume_router)



@app.get("/")
def root():
    return {
        "message": "ResumeOS API Running"
    }