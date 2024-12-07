from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Define TokenData for storing token-related information
class TokenData:
    def __init__(self, username: str = None):
        self.username = username