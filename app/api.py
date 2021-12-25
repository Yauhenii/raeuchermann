import logging
from typing import List

from fastapi import FastAPI, HTTPException
from psycopg2._psycopg import IntegrityError

from app.config import settings
from app.db.entry_handler import EntityHandler
from app.model import Entity

app = FastAPI()
logger = logging.getLogger("uvicorn.error")

entity_handler = EntityHandler(
    host=settings.db.HOST,
    port=settings.db.PORT,
    user_name=settings.POSTGRES_USER,
    password=settings.POSTGRES_PASSWORD,
    table_name=settings.db.TABLE_ENTITY_NAME,
)


@app.get("/entity/get/by-name/{name}", response_model=List[Entity])
async def get_entity_by_name(name):
    try:
        entity_list = entity_handler.select_entity_by_name([name])
        logger.info(entity_list)
        return entity_list
    except IndexError as exception:
        raise HTTPException(status_code=404, detail="no entities found") from exception


@app.post("/entity/post/name={name}&number={number}&date={date}")
async def post_entity_by_index(name, number, date):
    try:
        entity = entity_handler.insert_entity([name, number, date])
        logger.info(entity)
        return entity
    except IntegrityError as exception:
        raise HTTPException(
            status_code=404, detail="this entity already exists"
        ) from exception
