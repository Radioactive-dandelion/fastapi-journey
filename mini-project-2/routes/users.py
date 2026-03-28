from fastapi import APIRouter, HTTPException
from models.users import User, UserSignIn
from database.connection import Database

user_router = APIRouter()
db = Database(User)

@user_router.post("/user/signup")
async def signup(user: User):
    existing = await User.find_one(User.email == user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    return await db.save(user)

@user_router.post("/user/signin")
async def signin(credentials: UserSignIn):
    user = await User.find_one(User.email == credentials.email)
    if not user or user.password != credentials.password:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"detail": "Signed in successfully"}