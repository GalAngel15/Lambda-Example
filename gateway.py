from fastapi import FastAPI
import requests
from pydantic import BaseModel

app = FastAPI()

class AddRequest(BaseModel):
    name: str
    num1: int
    num2: int

@app.post("/add")
async def call_lambda(body: AddRequest):
    body_dict = body.model_dump()
    response = requests.post("http://127.0.0.1:3000/add", json=body_dict)
    return response.json()

@app.get("/hello")
async def say_hello():
    response = requests.get("http://127.0.0.1:3000/hello")
    return response.json()