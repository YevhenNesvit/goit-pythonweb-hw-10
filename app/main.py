from fastapi import FastAPI
from .database import engine, Base
from .routers import contacts, auth

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(contacts.router)
