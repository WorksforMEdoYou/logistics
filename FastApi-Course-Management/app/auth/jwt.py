from datetime import datetime, timedelta
import secrets
from jose import jwt
from passlib.context import CryptContext

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from .oauth2 import oauth2_scheme
from .oauth2 import TokenData
from ..models.mysql_models import Subscriber
from ..database.mysql import SessionLocal

# Secure Secret Key Configuration
SECRET_KEY = secrets.token_hex(32)  # Generates a 64-character (256-bit) hex key
ALGORITHM = "HS256" # Hashing variant
ACCESS_TOKEN_EXPIRE_MINUTES = 20

# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to create JWT access tokens
def create_access_token(data: dict, expires_delta: timedelta = None):
    """
    Creates a JWT access token with an expiration time.

    Args:
        data (dict): The payload data to encode into the token.
        expires_delta (timedelta, optional): Custom expiration time.

    Returns:
        str: Encoded JWT token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Function to verify a password against a hashed password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies that a plain password matches a hashed password.

    Args:
        plain_password (str): The plaintext password.
        hashed_password (str): The hashed password.

    Returns:
        bool: True if the passwords match, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

# Function to hash a password
def get_password_hash(password: str) -> str: 
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

# Function to get the current user from the token
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    db = SessionLocal()
    user = db.query(Subscriber).filter(Subscriber.email == token_data.username).first()
    if user is None:
        raise credentials_exception
    return user