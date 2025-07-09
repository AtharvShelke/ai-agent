import os
from fastapi import FastAPI
API_KEY = os.getenv("API_KEY")
app = FastAPI()

@app.get("/")

def read_index():
    return {
        "message":"This is a hello message",
        "API_KEY": API_KEY}