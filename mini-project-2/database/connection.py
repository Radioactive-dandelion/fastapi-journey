import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings
from typing import Type, List
from beanie import Document

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()

async def initialize_database(documents: List[Type[Document]]):
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    await init_beanie(database=client.get_default_database(), document_models=documents)

class Database:
    def __init__(self, model: Type[Document]):
        self.model = model

    async def save(self, document: Document):
        await document.insert()
        return document

    async def get(self, id: str):
        return await self.model.get(id)

    async def get_all(self):
        return await self.model.find_all().to_list()

    async def update(self, id: str, body: dict):
        doc = await self.model.get(id)
        if doc:
            await doc.update({"$set": body})
        return doc

    async def delete(self, id: str):
        doc = await self.model.get(id)
        if doc:
            await doc.delete()
        return doc