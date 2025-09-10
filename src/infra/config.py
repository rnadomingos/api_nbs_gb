from pydantic import PostgresDsn, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 5    
    DOMAIN: str = "localhost"

    # Postgres Conn
    POSTGRES_SCHEMA: str = "postgresql+psycopg"
    POSTGRES_USER: str 
    POSTGRES_PASSWORD: str 
    POSTGRES_SERVER: str 
    POSTGRES_PORT: int = 5432 
    POSTGRES_DB: str     

    # Oracle Conn
    ORACLE_USERNAME: str
    ORACLE_PASSWORD: str
    ORACLE_HOST: str
    ORACLE_PORT: int
    ORACLE_SERVICE: str
    ORACLE_DRIVER: str



    @computed_field
    @property
    def server_host(self) -> str:
        return f"https://{self.DOMAIN}"
    
    @computed_field
    @property
    def SQLALCHEMY_POSTGRES_URL(self) -> str | PostgresDsn:
        return  MultiHostUrl.build(
            scheme=self.POSTGRES_SCHEMA,
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB
        ) # type: ignore
    

    @computed_field
    @property
    def SQLALCHEMY_ORACLE_URL(self) -> str:
        return f"oracle+oracledb://{self.ORACLE_USERNAME}:{self.ORACLE_PASSWORD}@{self.ORACLE_HOST}:{self.ORACLE_PORT}/?service_name={self.ORACLE_SERVICE}"
    
    @computed_field
    @property
    def SQLALCHEMY_ORACLE_DRIVER(self) -> str:
        return f"{self.ORACLE_DRIVER}"


settings = Settings() # type: ignore 