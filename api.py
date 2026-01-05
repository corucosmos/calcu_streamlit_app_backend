# backend/api.py
import os
from fastapi import FastAPI, HTTPException, Header, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
from logic import Calculadora

app = FastAPI(title="API Backend")

# --- CONFIGURACIÓN DESDE SECRETOS ---
SECRET_KEY = os.getenv("BACKEND_SECRET_KEY", "dev-secret-123")
API_AUTH_KEY = os.getenv("API_AUTH_KEY", "clave-api-frontend-56789")
origins_raw = os.getenv("CORS_ORIGINS", "http://localhost:8501")
origins = [o.strip() for o in origins_raw.split(",")]

# --- MIDDLEWARES ---
app.add_middleware(SessionMiddleware, secret_key=SECRET_KEY) # Para historial
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True, # Importante para sesiones
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic
class OperacionRequest(BaseModel):
    a: float
    b: float
    operacion: str

def verificar_api_key(x_api_key: str = Header(None)):
    if x_api_key != API_AUTH_KEY:
        raise HTTPException(status_code=403, detail="No autorizado")
        
# Rutas de la API
@app.get("/")
def read_root():
    return {"message": "API Backend funcionando"}

@app.post("/calcular")
def calcular(request: OperacionRequest, r: Request, auth=Depends(verificar_api_key)):
    try:
        metodo = getattr(Calculadora, request.operacion)
        resultado = metodo(request.a, request.b)
        
        # Guardar en historial de sesión (usa SECRET_KEY para firmar)
        historial = r.session.get("historial", [])
        historial.append(f"{request.a} {request.operacion} {request.b} = {resultado}")
        r.session["historial"] = historial[-5:] # Últimas 5
        
        return {
            "resultado": resultado,
            "operacion": request.operacion,
            "a": request.a,
            "b": request.b
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/historial")
def ver_historial(r: Request, auth=Depends(verificar_api_key)):
    return {"historial": r.session.get("historial", [])}

@app.get("/health")
def health_check():
    return {"status": "healthy"}