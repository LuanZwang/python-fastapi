from fastapi import FastAPI
from api.endpoints.controllers import user_endpoints, enchentes_endpoints

app = FastAPI()

app.include_router(user_endpoints.router)
app.include_router(enchentes_endpoints.router)