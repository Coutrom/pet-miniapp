from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

pet = {"health": 100, "mood": 100}

class Action(BaseModel):
    action: str

@app.get("/api/status")
def status():
    return pet

@app.post("/api/action")
def action(a: Action):
    if a.action == "feed":
        pet["health"] += 5
    if a.action == "play":
        pet["mood"] += 5
    if a.action == "sleep":
        pet["health"] += 2
    return pet
