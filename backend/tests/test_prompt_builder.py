import database.model_registry


from database.connection import get_db_session

from repositories.user_repository import UserRepository

from services.prompt_builder import PromptBuilder

db = get_db_session()

user = UserRepository.get_by_email(
    db,
    "madhusudan.dsdev@gmail.com"
)

prompt = PromptBuilder.build_resume_prompt(
    user,
    "We are looking for a Data Scientist with Python, SQL, AWS and Machine Learning experience."
)

print(prompt)

db.close()