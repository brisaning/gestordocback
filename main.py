from fastapi import FastAPI
#from src.application.router import router as trd_router
from src.application.routers.series_router import router as series_router
from src.application.routers.subseries_router import router as subseries_router
from src.application.routers.tipos_documentales_router import router as tipos_documentales_router

app = FastAPI()

apiPrefix = "/api"
apiVersion = "/v1"

app.include_router(series_router, prefix= apiPrefix + apiVersion + "/trd", tags=["TRD"])
app.include_router(subseries_router, prefix= apiPrefix + apiVersion + "/trd", tags=["TRD"])
app.include_router(tipos_documentales_router, prefix= apiPrefix + apiVersion + "/trd", tags=["TRD"])
#app.include_router(trd_router, prefix= apiPrefix + apiVersion + "/trd", tags=["TRD"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Management API"}
