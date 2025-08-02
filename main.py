from fastapi import FastAPI
from app.routers import auth, users, appointments, websocket
from app.database.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Telemedicine API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(appointments.router)
app.include_router(websocket.router)
