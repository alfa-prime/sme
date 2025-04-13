from fastapi import APIRouter
from typing import Annotated

from sqlalchemy import func # noqa
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession # noqa
from fastapi import Depends
from app.db import get_session

router = APIRouter(prefix="/health")


@router.get("/ping")
async def pong():
    return {"ping": "pong"}


@router.get("/db")
async def ping_db(session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        await session.execute(select(1))
        return {"status": "ok", "message": "База данных доступна"}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.get("/version")
async def get_db_version(session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        result = await session.execute(select(func.version()))
        version = result.scalar()
        return {"status": "ok", "version": version}
    except Exception as e:
        return {"status": "error", "message": str(e)}
