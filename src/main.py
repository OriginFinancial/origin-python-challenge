from fastapi import FastAPI

from src.controllers import pokemon

app = FastAPI(
    title="Origin Python Challenge",
    description="Python challenge for backend candidates",
    version="0.1.0",
)

routers = [pokemon]
for router in routers:
    app.include_router(router.router)
