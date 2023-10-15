from pydantic import BaseModel, SecretStr

class UserDetails(BaseModel):
    username: str
    password: SecretStr

user_details = UserDetails(username='Steve', password=SecretStr('secret'))

print(user_details)
