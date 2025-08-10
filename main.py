from fastapi import FastAPI
from src.application.routers.series_router import router as series_router
from src.application.routers.subseries_router import router as subseries_router
from src.application.routers.tipos_documentales_router import router as tipos_documentales_router

apiPrefix = "/api/v1"

app = FastAPI(
    openapi_prefix=apiPrefix,
    tags=["Document Management API"],
    contact={
        "name": "Brian Sanabria",
        "email": "  brisaning@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    title="Document Management API",
    description="A API to manage documents",
    version="1.0.0",
)



app.include_router(series_router, prefix=apiPrefix)
app.include_router(subseries_router, prefix=apiPrefix)
app.include_router(tipos_documentales_router, prefix=apiPrefix)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Management API"}
