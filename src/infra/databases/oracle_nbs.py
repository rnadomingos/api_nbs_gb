import oracledb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.infra.config import settings


oracledb.init_oracle_client(lib_dir=f"{settings.SQLALCHEMY_ORACLE_DRIVER}")

SQLALCHEMY_ORACLE_URL = settings.SQLALCHEMY_ORACLE_URL

engine = create_engine(
  str(SQLALCHEMY_ORACLE_URL)
)

sessionOracleLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

