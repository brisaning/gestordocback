from fastapi import FastAPI
from src.application.routers.series_router import router as series_router
from src.application.routers.subseries_router import router as subseries_router
from src.application.routers.tipos_documentales_router import router as tipos_documentales_router

app = FastAPI()



app.include_router(series_router)
app.include_router(subseries_router)
app.include_router(tipos_documentales_router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Management API"}
