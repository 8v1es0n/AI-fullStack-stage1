from datetime import datetime

from fastapi import Depends, APIRouter

import logging
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import *
from app.schemas import *
from app.utils import get_now



session_router = APIRouter(prefix="/api", tags=["会话信息"])

# 创建会话
@session_router.post("/sessions")
async def create_sessions(sessions : RequestSessions, session: AsyncSession = Depends(get_session)):
    session_name = get_now()
    ai_session = AiSession(session_name=session_name, nick_name=sessions.nick_name, nature=sessions.nature,
                           create_time=datetime.now(), update_time=datetime.now())
    session.add(ai_session)
    # 提交修改
    await session.commit()

    # 3. 给前端响应
    return Result(code = 200, message = "创建会话成功", data = session_name)


# 删除会话
@session_router.delete("/sessions/{session_name}")
async def delete_sessions(session_name : str, session: AsyncSession = Depends(get_session)):
    # 查询基本信息
    session_result = await session.execute(select(AiSession).where(AiSession.session_name == session_name))
    ai_session = session_result.scalars().one()

    # 删除该条对应的会话内容
    await session.execute(delete(AiMessage).where(AiMessage.session_id == ai_session.id))
    # 删除会话基本信息
    await session.execute(delete(AiSession).where(AiSession.id == ai_session.id))
    # 提交事务
    await session.commit()

    # 3. 给前端响应
    return Result(code = 200, message = "删除会话成功", data = None)

# 获取会话列表
@session_router.get("/sessions")
async def get_sessions_list(session: AsyncSession = Depends(get_session)):
    logging.info("获取会话列表")
    session_result = await session.execute(select(AiSession.session_name)
                                           .order_by(AiSession.session_name.desc()))
    session_list = session_result.scalars().all()
    return Result(code=200, message="会话列表加载成功", data = session_list)


# 获取指定会话
@session_router.get("/sessions/{session_name}", summary="获取指定会话信息")
async def get_sessions_byid(session_name : str, session: AsyncSession = Depends(get_session)):
    # 获取会话基本数据
    session_result = await session.execute(select(AiSession).where(AiSession.session_name == session_name))
    ai_session = session_result.scalars().one()

    # 获取会话内容
    message_result = await session.execute(select(AiMessage).where(AiMessage.session_id == ai_session.id))
    ai_messages = message_result.scalars().all()

    #3.组装数据
    session_data={
        "nick_name":ai_session.nick_name,
        "nature":ai_session.nature,
        "session_name":ai_session.session_name,
        "messages":[{"role":i.role,"content":i.content} for i in ai_messages]
    }
    # 将数据返回给前端
    return Result(code = 200, message = "加载会话成功", data = session_data)