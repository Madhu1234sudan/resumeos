from core.security import (
    create_access_token,
    decode_access_token
)

token = create_access_token(
    {
        "sub": "test@example.com"
    }
)

print("\nTOKEN:")
print(token)

print("\nDECODED:")
print(
    decode_access_token(token)
)