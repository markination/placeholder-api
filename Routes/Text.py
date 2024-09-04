import os
import json
import traceback
from fastapi import APIRouter, Form
from starlette.requests import Request
from starlette.responses import Response, JSONResponse
import random
import string
from wonderwords import RandomSentence

class StringsRouter(APIRouter):
    def __init__(self):
        super().__init__(tags=["Strings"])  

    async def on_strings_gibberish(request: Request, characters: int):
        try:
            result_str = ''.join(random.choice(string.ascii_letters) for i in range(characters))
            return JSONResponse(status_code=200, content={"message": result_str})
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": f"{e}"})
    
    async def on_strings_sentence(request: Request):
        try:
            s = RandomSentence()
            sentence = s.sentence()
            return JSONResponse(status_code=200, content={"message": f"{sentence}"})
        except Exception as e:
            return JSONResponse(status_code=500, content={"message": f"{e}"})
        
        


router = StringsRouter()
router.get("/gibberish", description="Generate some gibberish")(StringsRouter.on_strings_gibberish)
router.get("/sentence", description="Generate a sentence")(StringsRouter.on_strings_sentence)