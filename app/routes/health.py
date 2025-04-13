from fastapi import APIRouter

router = APIRouter(prefix="/health")


@router.get("/ping")
async def pong():
    return {"ping": "pong"}
