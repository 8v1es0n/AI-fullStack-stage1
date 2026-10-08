from fastapi import Depends, APIRouter
from fastapi.encoders import jsonable_encoder

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.db import *
from app.schemas import *


preset_router = APIRouter(prefix="/api", tags=["伴侣预设信息"])

# 读取预设返回信息
@preset_router.get("/presets")
async def get_presets(session: AsyncSession = Depends(get_session)):
    # 查询ai_preset表
    result = await session.execute(select(AiPreset).order_by(AiPreset.sort_order.asc()))
    # 获取到的数据进行json序列化
    preset_list = jsonable_encoder(result.scalars().all())
    # 返回结果给前端
    return Result(code=200, message="预设信息加载成功", data=preset_list)