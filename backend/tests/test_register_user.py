import models

from database.connection import get_db_session

from services.auth_service import AuthService


db = get_db_session()

try:

    user = AuthService.register_user(
        db=db,
        full_name="Test User",
        email="test@example.com",
        password="ResumeOS123"
    )

    print("User Created")

    print(user.id)
    print(user.email)

finally:
    db.close()