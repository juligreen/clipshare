from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel


class Message(BaseModel):
    content: str

app = FastAPI()

app.mount("/static/", StaticFiles(directory="static"), name="static")

messages = []

@app.post("/send/")
async def post_content(message: Message):
    messages.append(message.content)
    return message

@app.get("/request/")
async def get_content():
    return messages
