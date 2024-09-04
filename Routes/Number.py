import os
import json
import traceback
from fastapi import APIRouter, Form
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
import random

class NumberRouter(APIRouter):
    def __init__(self):
        super().__init__(tags=["Strings"])  

    async def on_number_random(request: Request,min_number:int, max_number:int):
        try:
            return JSONResponse(status_code=200, content={"message": random.randint(min_number, max_number)})
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": f"{e}"})

router = NumberRouter()
router.get("/random", description="Generate a random number")(NumberRouter.on_number_random)