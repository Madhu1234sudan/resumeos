from database.connection import get_db_session

from models.user import User
from models.skill import Skill
from models.project import Project


db = get_db_session()

try:

    project = (
        db.query(Project)
        .filter(
            Project.project_name ==
            "AI-Powered Resume Screening and Job Matching System"
        )
        .first()
    )

    skills = (
        db.query(Skill)
        .filter(
            Skill.skill_name.in_(
                [
                    "Python",
                    "SQL",
                    "Machine Learning"
                ]
            )
        )
        .all()
    )

    for skill in skills:
        project.skills.append(skill)

    db.commit()

    print("Project-Skill mapping created.")

finally:
    db.close()