from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel
import deepcut

app = FastAPI()

class Passage(BaseModel):
    text: str
    custom_words: Optional[List[str]] = None

@app.post("/")
async def cut_passage(passage: Passage):
    arr = deepcut.tokenize(passage.text, passage.custom_words)
    return { "result" : arr }

