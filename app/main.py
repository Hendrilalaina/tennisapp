from typing import Annotated
from fastapi import FastAPI, File, Form, UploadFile

from app.routers import routers
from app.db.models import init_db

app = FastAPI(
    title="Tennis Application Management API",
    description="Managing tennis tournament",
    version="1.0.0")

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

init_db()
for router in routers:
    app.include_router(router)

@app.get("/")
async def welcome():
    return "Welcome to tennis app"

@app.post("/files/")
async def create_file(
    file: Annotated[UploadFile, File()],
):
    try:
        file_path = './upload/{file.filename}'
        with open(file_path, 'wb') as f:
            f.write(file.file.read())
        return {'message': 'File uploaded'}

    except Exception as e:
        return {'message': e.args}