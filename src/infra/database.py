from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.infra.config import settings

SQLALCHEMY_POSTGRES_URL = settings.SQLALCHEMY_POSTGRES_URL

engine = create_engine(
  str(SQLALCHEMY_POSTGRES_URL)
)

sessionLocal = sessionmaker(autocommit = False, autoflush=False, bind=engine)

Base = declarative_base()