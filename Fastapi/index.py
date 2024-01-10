import random
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/random')
async def get_random():
    rn: int = random.randint(0, 100)
    return {'num': rn, 'limit': 100}