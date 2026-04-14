from fastapi import APIRouter, HTTPException
from models.events import Event, EventUpdate
from database.connection import Database

event_router = APIRouter()
db = Database(Event)

@event_router.get("/event/")
async def get_events():
    return await db.get_all()

@event_router.get("/event/{id}")
async def get_event(id: str):
    event = await db.get(id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

@event_router.post("/event/new")
async def create_event(event: Event):
    return await db.save(event)

@event_router.put("/event/{id}")
async def update_event(id: str, event: EventUpdate):
    updated = await db.update(id, event.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated

@event_router.delete("/event/{id}")
async def delete_event(id: str):
    deleted = await db.delete(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"detail": "Event deleted"}