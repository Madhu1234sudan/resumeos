from database.connection import get_db_session

from models.user import User
from models.project import Project
from models.skill import Skill


db = get_db_session()

try:

    user = (
        db.query(User)
        .filter(
            User.email == "madhusudan.dsdev@gmail.com"
        )
        .first()
    )

    if not user:
        print("User not found.")
        exit()

    project = Project(
        project_name="AI-Powered Resume Screening and Job Matching System",
        description="""
Built an intelligent resume screening and job matching system
using NLP, TF-IDF, cosine similarity, and machine learning.
Supports resume upload, JD upload, candidate ranking,
skill extraction, and semantic matching.
""",
        github_url=""
    )

    user.projects.append(project)

    db.commit()

    print("Project inserted successfully.")

finally:
    db.close()