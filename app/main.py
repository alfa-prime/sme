from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routes import router_health


@asynccontextmanager
async def lifespan(app: FastAPI):  # noqa
    # Здесь можно делать подключение к базе, инициализацию и т.п.
    print("🌱 Starting up...")
    yield
    print("🧹 Shutting down...")


app = FastAPI(title="FastAPI Admin", lifespan=lifespan)
app.include_router(router_health)
