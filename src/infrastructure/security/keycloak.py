from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests

load_dotenv()

KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")


class User(BaseModel):
    username: str
    roles: list[str] = []

def get_keycloak_public_key():
    return requests.get(f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}").json()["public_key"]

oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth",
    tokenUrl=f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token"
)

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        public_key = f"-----BEGIN PUBLIC KEY-----\n{get_keycloak_public_key()}\n-----END PUBLIC KEY-----"
        payload = jwt.decode(token, public_key, algorithms=["RS256"], options={"verify_aud": False})
        username: str = payload.get("preferred_username")
        roles: list[str] = payload.get("realm_access", {}).get("roles", [])
        if username is None:
            raise credentials_exception
        return User(username=username, roles=roles)
    except JWTError:
        raise credentials_exception
