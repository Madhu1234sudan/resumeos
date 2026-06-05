import models
from database.connection import get_db_session

from repositories.user_repository import UserRepository


db = get_db_session()

try:

    user = UserRepository.get_by_email(
        db,
        "madhusudan.dsdev@gmail.com"
    )

    print(user)

finally:
    db.close()