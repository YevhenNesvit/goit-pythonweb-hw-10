from fastapi import FastAPI
from .database import engine, Base
from .routers import contacts

# Створення таблиць
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Підключення маршруту
app.include_router(contacts.router)
