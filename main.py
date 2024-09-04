import sys
import dotenv
dotenv.load_dotenv() 

sys.dont_write_bytecode = True
import os
import asyncio
import logging
from fastapi import FastAPI
import uvicorn
from Routes import Text, Number

dotenv.load_dotenv()

app = FastAPI()
app.include_router(Text.router, prefix="/text")
app.include_router(Number.router, prefix="/number")

@app.on_event("startup")
async def startup_event():
    print("HackClub is cool..")
  
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5050, log_level="info")

