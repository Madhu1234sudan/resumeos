from database.connection import get_db_session

from models.user import User
from models.skill import Skill
from models.project import Project

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

    jd_skills = [
        "Python",
        "Machine Learning",
        "Statistics",
        "Pandas"
    ]

    result = MatchingEngine.match_skills(
        profile_skills,
        jd_skills
    )

    print("\nProfile Skills:")
    print(profile_skills)

    print("\nResult:")
    print(result)

finally:
    db.close()