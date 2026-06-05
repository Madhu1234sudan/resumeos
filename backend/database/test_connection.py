from sqlalchemy import text
from connection import engine

try:
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT current_database();")
        )

        print(
            "Connected to:",
            result.scalar()
        )

except Exception as e:
    print("Connection Error:", e)