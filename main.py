from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

app = FastAPI()

model = SentenceTransformer("all-MiniLM-L6-v2")

class RequestModel(BaseModel):
    text: Union[str, List[str]]

@app.post("/embedding")
def get_embedding(req: RequestModel):
    embedding = model.encode(req.text).tolist()
    return {"embedding": embedding}