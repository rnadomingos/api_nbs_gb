from sqlalchemy import Column, Boolean, Integer, String
from infra.databases.postgres import Base

class User(Base):

    __tablename__ = "account_users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default='common')
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)