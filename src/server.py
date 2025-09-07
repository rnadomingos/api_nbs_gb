from datetime import timedelta
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.infra.middleware.deps import SessionDep, CurrentUser
from src.data.schemas import Token
from src.controller import accounts
from src.infra import security
from src.infra.config import settings

app = FastAPI()

@app.post("/login")
async def login(
    session: SessionDep,
    form_data: Annotated[OAuth2PasswordRequestForm,Depends()]
) -> Token:
    
    user = accounts.authenticate(
        db=session, username=form_data.username, password=form_data.password
    )

    if not user: 
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={ "WWW-Authenticate": "Bearer" },
        )
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    return Token(
        access_token=security.create_access_token(
            user.id, expiries_delta=access_token_expires # type: ignore
        )
    )