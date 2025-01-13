from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.db import init_db, close_db
from src.routes.routes import router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown
    await close_db()

app = FastAPI(lifespan=lifespan)

app.include_router(router)