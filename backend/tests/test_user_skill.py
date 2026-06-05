# backend/tests/test_user_skill.py

from database.connection import get_db_session
from models.user import User
from models.skill import Skill
from models.project import Project

db = get_db_session()

try:

    existing_user = (
        db.query(User)
        .filter(User.email == "madhusudan.dsdev@gmail.com")
        .first()
    )

    if not existing_user:

        user = User(
            full_name="Madhusudan Somvanshi",
            email="madhusudan.dsdev@gmail.com",
            phone="6360344476",
            linkedin_url="linkedin.com/in/madhusudan",
            github_url="github.com/madhusudan",
            location="Basavakalyan"
        )

        db.add(user)
        db.commit()

        print("User inserted successfully.")

    else:

        print("User already exists.")

finally:
    db.close()