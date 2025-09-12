from fastapi import FastAPI
from src.infra.databases.postgres import Base, engine 
from src.routes import auth_router, nbs_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Grand Brasil 🚗",
    description="Esta API retorna informações de veículos, entregas e agendamentos de serviço.",
    version="1.0.0",
    servers=[
        {"url": "http://api.grandbrasil.com.br:8050", "description": "Servidor Produção"},
        {"url": "http://192.168.16.28:8050", "description": "Servidor Local"},
        {"url": "http://127.0.0.1:8050", "description": "Servidor Dev"},
    ],
    contact={
        "name": "Tiveo Tecnologia",
        "url": "https://tiveo.com.br",
        "email": "suporte@tiveo.com.br",
    },
    
)

app.include_router(auth_router.router)
app.include_router(nbs_router.nbs_router)