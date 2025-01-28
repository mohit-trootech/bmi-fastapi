from fastapi import FastAPI
from routers.bmi import router

app = FastAPI()

app.include_router(router)
