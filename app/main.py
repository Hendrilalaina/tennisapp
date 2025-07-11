from fastapi import FastAPI

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