from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from src.infra.middleware.deps import SessionDep, CurrentUser
from src.data.schemas.user_schemas import Token, User, UserCreate
from src.infra.config import settings
from src.controller import accounts
from src.infra import security


router = APIRouter()

@router.post("/login", tags=["Auth"])
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

@router.post("/signup", response_model=User, tags=["Users"])
async def create_user(current_user: CurrentUser, session: SessionDep, user: UserCreate):
    """
    Route to create users. To create, the user must be admin. 
    """    
    verify_admin = current_user.is_admin

    if not verify_admin: # type: ignore
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")

    db_user = accounts.get_user(db=session, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Could not create account")
    return accounts.create_user(session, user)


@router.get("/users", response_model=list[User], tags=["Users"])
async def read_users(current_user: CurrentUser, session: SessionDep):
    """
    route to list users. 
    To list, the user must be admin. 
    """
    if not current_user.is_admin: # type: ignore
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized user")


    db_users = accounts.get_users(session)
    return db_users