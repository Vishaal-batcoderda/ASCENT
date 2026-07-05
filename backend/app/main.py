from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.stock import router as stock_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="ASCENT API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(stock_router)