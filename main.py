import sys
import dotenv
dotenv.load_dotenv() 

sys.dont_write_bytecode = True
import os
import asyncio
import logging
from fastapi import FastAPI
import uvicorn

dotenv.load_dotenv()

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    print("HackClub is cool..")
  
if __name__ == '__main__':
    uvicorn.run(app, host=os.getenv("host"), port=os.getenv("port"), log_level="info")

