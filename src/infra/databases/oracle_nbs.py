from typing import Annotated

import oracledb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from fastapi import Depends


from src.infra.config import settings

oracledb.init_oracle_client(lib_dir=f"{settings.ORACLE_DRIVER}")

SQLALCHEMY_ORACLE_URL = settings.SQLALCHEMY_ORACLE_URL

engine = create_engine(
  str(SQLALCHEMY_ORACLE_URL)
)

sessionOracleLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_oracle_db():
    db = sessionOracleLocal()
    try:
        yield db
    finally:
        db.close()

SessionOra = Annotated[Session, Depends(get_oracle_db)]