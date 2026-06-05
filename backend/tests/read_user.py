from database.connection import get_db_session

from models.user import User
from models.skill import Skill
from models.project import Project


db = get_db_session()

try:

    users = db.query(User).all()

    for user in users:
        print(f"ID: {user.id}")
        print(f"Name: {user.full_name}")
        print(f"Email: {user.email}")
        print("-" * 30)

finally:
    db.close()