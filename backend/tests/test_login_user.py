import models

from database.connection import get_db_session

from services.auth_service import AuthService


db = get_db_session()

try:

    result = AuthService.login_user(
        db=db,
        email="test@example.com",
        password="ResumeOS123"
    )

    print(result)

finally:
    db.close()