from fastapi import FastAPI
from app.models import User

app =  FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}

