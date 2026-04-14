from fastapi import FastAPI
from routes.events import event_router as events_router
from routes.users import user_router as users_router
from database.connection import initialize_database
from models.events import Event
from models.users import User

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await initialize_database([Event, User])

app.include_router(events_router)
app.include_router(users_router)