# coding: utf-8
import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/html/index.html")


@app.get("/home")
async def home():
    return FileResponse("static/html/home.html")


@app.get("/line")
async def line():
    return FileResponse("static/html/index.html")

@app.get("/line_content")
async def line_content():
    return FileResponse("static/html/line.html")

@app.get("/whatsapp")
async def whatsapp():
    return FileResponse("static/html/index.html")

@app.get("/whatsapp_content")
async def whatsapp_content():
    return FileResponse("static/html/whatsapp.html")

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8001, reload=True)
