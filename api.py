# backend/api.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from logic import Calculadora
from pydantic import BaseModel

app = FastAPI(title="API Backend")

# Configurar CORS para permitir conexiones desde Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelos Pydantic
class OperacionRequest(BaseModel):
    a: float
    b: float
    operacion: str

class UsuarioRequest(BaseModel):
    nombre: str
    email: str

# Rutas de la API
@app.get("/")
def read_root():
    return {"message": "API Backend funcionando"}

@app.post("/calcular")
def calcular(request: OperacionRequest):
    try:
        if request.operacion == "suma":
            resultado = Calculadora.suma(request.a, request.b)
        elif request.operacion == "resta":
            resultado = Calculadora.resta(request.a, request.b)
        elif request.operacion == "multiplicacion":
            resultado = Calculadora.multiplicacion(request.a, request.b)
        elif request.operacion == "division":
            resultado = Calculadora.division(request.a, request.b)
        else:
            raise HTTPException(status_code=400, detail="Operación no válida")
        
        return {
            "resultado": resultado,
            "operacion": request.operacion,
            "a": request.a,
            "b": request.b
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy"}