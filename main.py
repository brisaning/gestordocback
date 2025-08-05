from fastapi import FastAPI
from src.application.routers import router as trd_router

app = FastAPI()

app.include_router(trd_router, prefix="/trd", tags=["TRD"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Management API"}
