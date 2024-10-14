# -*- coding: utf-8 -*-
# Date: 2024/10/13
# Author: Jason
# File: server

from fastapi import FastAPI
import uvicorn

import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"[x] current ip address: {ip_address}")
app = FastAPI()

@app.get("/")
async def hello() -> str:
    return "hello!/n"

if __name__ == '__main__':
    # 将host设置为0.0.0.0，本地才可以访问

    uvicorn.run(app=app, host="0.0.0.0", port=8000)