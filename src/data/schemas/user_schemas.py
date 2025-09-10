from typing import List
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
      id: int
      role: str
      is_active: bool
      is_admin: bool

      class Config:
           from_attributes = True

class Users(BaseModel):
    users: List[User]           

class Token(BaseModel):
     access_token: str
     token_type: str = "bearer"           

class TokenPayload(BaseModel):
     sub: int | None = None