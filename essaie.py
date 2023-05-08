from argon2 import PasswordHasher
import jwt
import secure

token = secure.generate_token('webshop')
print(token)
