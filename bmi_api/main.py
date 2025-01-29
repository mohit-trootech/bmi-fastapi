from fastapi import FastAPI
from .routers.bmi import router as bmi_router
from .routers.users import router as users_router

app = FastAPI()

app.include_router(bmi_router)
app.include_router(users_router)
