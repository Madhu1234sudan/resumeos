from core.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)


password = "ResumeOS123"


hashed_password = hash_password(
    password
)

print("\nHASHED PASSWORD:")
print(hashed_password)


is_valid = verify_password(
    password,
    hashed_password
)

print("\nPASSWORD VALID:")
print(is_valid)


token = create_access_token(
    {
        "sub": "madhusudan.dsdev@gmail.com"
    }
)

print("\nJWT TOKEN:")
print(token)


decoded = decode_access_token(
    token
)

print("\nDECODED TOKEN:")
print(decoded)