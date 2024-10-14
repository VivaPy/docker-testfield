# -*- coding: utf-8 -*-
# Date: 2024/10/13
# Author: Jason
# File: server

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def hello() -> str:
    return "hi!"

if __name__ == '__main__':
    uvicorn.run(app=app, port=8000)