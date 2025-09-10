from fastapi import FastAPI
from src.infra.databases.postgres import Base, engine 
from src.routes import auth_router, nbs_router


Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(auth_router.router)
app.include_router(nbs_router.nbs_router)