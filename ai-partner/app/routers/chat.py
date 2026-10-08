from datetime import datetime

from fastapi import Depends, APIRouter

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import *
from app.schemas import *
from app.ai import *



chat_router = APIRouter(prefix="/api", tags=["AI交互信息"])

# 聊天功能
@chat_router.post("/chat")
async def ai_chat(chat : RequestChat, session: AsyncSession = Depends(get_session)):
    # 从数据库中读取会话基本信息
    session_result = await session.execute(select(AiSession).where(AiSession.session_name == chat.session_name))
    ai_session = session_result.scalars().one()

    # 从数据库中读取会话内容
    message_result = await session.execute(select(AiMessage).where(AiMessage.session_id == ai_session.id))
    ai_messages = message_result.scalars().all()

    # 组织角色信息
    # 跟新系统提示词
    if len(ai_messages) == 0:
        session.add(AiMessage(session_id= ai_session.id, role= "system",
                              content= SYSTEM_PROMPT_TEMPLATE % (chat.nick_name, chat.nature),
                              create_time=datetime.now()))
    else:
        await session.execute(update(AiMessage)
                              .where(AiMessage.session_id == ai_session.id, AiMessage.role == "system")
                              .values(content= SYSTEM_PROMPT_TEMPLATE % (chat.nick_name, chat.nature)))
    # 添加用户提示词
    session.add(AiMessage(session_id= ai_session.id, role= "user", content= chat.message, create_time=datetime.now()))
    # 同步变更到数据库
    await session.flush()

    # 读取所有会话内容, 查询ai_message表
    result = await session.execute(select(AiMessage.role, AiMessage.content)
                                   .where(AiMessage.session_id == ai_session.id)
                                   .order_by(AiMessage.create_time.asc()))
    # 获取到的数据进行json序列化
    messages = result.all()
    history_list = [{"role": msg.role, "content": msg.content} for msg in messages]

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=history_list,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "disabled"}}
    )
    assistant = response.choices[0].message.content
    # 添加大模型返回的信息
    session.add(AiMessage(session_id= ai_session.id, role= "assistant", content= assistant, create_time=datetime.now()))

    # 更新人设信息
    await session.execute(update(AiSession).where(AiSession.session_name == chat.session_name)
                          .values(nick_name=chat.nick_name, nature=chat.nature, update_time=datetime.now()))
    # 提交数据
    await session.commit()

    return Result(code = 200, message = "对话信息返回成功", data=assistant)