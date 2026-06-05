from database.connection import get_db_session

from models.user import User
from models.skill import Skill
from models.project import Project

from services.jd_analyzer import JDAnalyzer
from services.matching_engine import MatchingEngine


db = get_db_session()

try:

    user = (
        db.query(User)
        .filter(
            User.email ==
            "madhusudan.dsdev@gmail.com"
        )
        .first()
    )

    profile_skills = [
        skill.skill_name
        for skill in user.skills
    ]

    job_description = """
    We are looking for a Data Scientist
    with strong skills in Python,
    SQL, Pandas, Machine Learning,
    Statistics and AWS.
    """

    jd_skills = (
        JDAnalyzer.extract_skills(
            job_description
        )
    )

    result = (
        MatchingEngine.match_skills(
            profile_skills,
            jd_skills
        )
    )

    print("\nPROFILE SKILLS")
    print(profile_skills)

    print("\nJD SKILLS")
    print(jd_skills)

    print("\nMATCH RESULT")
    print(result)

finally:
    db.close()