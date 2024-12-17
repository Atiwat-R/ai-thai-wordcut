from fastapi import FastAPI
from pydantic import BaseModel
import deepcut

app = FastAPI()

class Passage(BaseModel):
    text: str

@app.post("/")
async def cut_passage(passage: Passage):
    arr = deepcut.tokenize(passage.text)
    return { "result" : arr }

