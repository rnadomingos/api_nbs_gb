from fastapi import FastAPI
from src.infra.database import Base, engine 
from src.routes.router import router 


Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(router)