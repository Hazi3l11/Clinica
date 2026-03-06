from fastapi import FastAPI
from app.controllers.routes import router as clinica_router

app = FastAPI(title="API Clínica")

# Incluir las rutas del controlador
app.include_router(clinica_router, prefix="/api")

@app.get("/")
def home():
    return {"status": "API Clínica funcionando en WSL"}