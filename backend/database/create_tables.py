from database.connection import engine
from database.base import Base


from models.user import User
from models.skill import Skill
from models.project import Project
from models.project_skill import ProjectSkill


Base.metadata.create_all(bind=engine)

print("Tables created successfully.")