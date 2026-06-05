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

    if not user:
        print("User not found.")
        exit()

    skills = [
        ("Python", "Programming", "Advanced"),
        ("SQL", "Database", "Intermediate"),
        ("Machine Learning", "AI/ML", "Intermediate")
    ]

    for name, category, level in skills:

        skill = Skill(
            skill_name=name,
            category=category,
            proficiency_level=level
        )

        user.skills.append(skill)

    db.commit()

    print("Skills added successfully.")

finally:
    db.close()