from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from pydantic import ValidationError

from infra.databases.postgres import sessionLocal
from src.infra.config import settings
from src.data.schemas import TokenPayload
from src.data.models import User

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Annotated[str, Depends(oauth2)]

async def get_current_user(session: SessionDep, token: TokenDep) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except(JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid credentials"
        )
    
    user = session.get(User, token_data.sub)

    if user is None:
        raise HTTPException( status_code=404, detail="User not found")
    
    if not user.is_active: # type: ignore
        raise HTTPException(status_code=400, detail="Inactive user.")
    
    return user

CurrentUser = Annotated[User, Depends(get_current_user)]