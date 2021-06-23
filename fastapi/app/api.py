from fastapi import FastAPI, File, UploadFile
from app.models.entityModel import entity
from app.services.databasecon import insert_Answers
from typing import List
import datetime
import shutil


app = FastAPI()
path = "files"


@app.get("/")
async def root():
    return {"message": "Server is up"}


@app.post("/update/entity")
async def create_upload_file(item: entity):
    print(item.id)
    response = insert_Answers(item.id, item.temperature.value, item.pressure.value, item.time.value)
    return response