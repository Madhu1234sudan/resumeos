from database.connection import get_db_session

from models.user import User
from models.skill import Skill
from models.project import Project


db = get_db_session()

try:

    user = (
        db.query(User)
        .filter(
            User.email == "madhusudan.dsdev@gmail.com"
        )
        .first()
    )

    print(f"\nUser: {user.full_name}")
    print("\nSkills:")

    for skill in user.skills:
        print(
            f"- {skill.skill_name} "
            f"({skill.category})"
        )

finally:
    db.close()