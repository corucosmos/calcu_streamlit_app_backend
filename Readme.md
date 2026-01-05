# ⚙️ Calculadora API (Backend)

Servidor de alto rendimiento construido con **FastAPI** que gestiona la lógica matemática y la seguridad de la aplicación.

## 🚀 Funcionalidades
- **Cálculo Seguro:** Procesa operaciones matemáticas básicas.
- **Gestión de Sesiones:** Utiliza `SessionMiddleware` para mantener un historial de operaciones por usuario sin necesidad de base de datos.
- **Seguridad por API Key:** Validación obligatoria de cabeceras para permitir peticiones.
- **CORS Dinámico:** Configurado a través de variables de entorno para permitir solo orígenes autorizados.

## 🛠️ Requisitos
- Python 3.9+
- FastAPI
- Uvicorn
- Starlette (para gestión de sesiones)

## 🔧 Variables de Entorno
| Variable | Descripción |
| :--- | :--- |
| `BACKEND_SECRET_KEY` | Llave maestra para cifrar las cookies del historial. |
| `API_AUTH_KEY` | Clave que el backend espera recibir en el header `x-api-key`. |
| `CORS_ORIGINS` | Lista de URLs permitidas (ej: `http://localhost:8501`). |

## 🚀 Ejecución Local
```bash
# Instalar dependencias
pip install fastapi uvicorn starlette pydantic

# Ejecutar servidor
export BACKEND_SECRET_KEY="tu_clave_local"
export API_AUTH_KEY="clave_api_local"
uvicorn api:app --host 0.0.0.0 --port 8000 --reload