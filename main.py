from fastapi import FastAPI

from src.api.v1 import routers

app = FastAPI()

for router in routers:
    app.include_router(router)

