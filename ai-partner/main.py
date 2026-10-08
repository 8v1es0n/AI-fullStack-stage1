from datetime import datetime
import json
import os
from typing import Any

from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder
from openai import OpenAI
from pydantic import BaseModel
import logging
from fastapi import Request
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from db import session_factory, AiPreset, AiSession, AiMessage

# 配置日志
logging.basicConfig(

    # 日志级别
    level=logging.INFO,
    # 日志输出格式
    format = "%(asctime)s - %(levelname)s - [%(filename)s : %(lineno)d] - %(message)s"
)



app = FastAPI()

# 系统提示词模板
SYSTEM_PROMPT_TEMPLATE = """你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。
    规则：
        1. 每次只回1条消息
        2. 禁止任何场景或状态描述性文字
        3. 匹配用户的语言
        4. 回复简短，像微信聊天一样
        5. 有需要的话可以用❤️🌸等emoji表情
        6. 用符合伴侣性格的方式对话
        7. 回复的内容, 要充分体现伴侣的性格特征
        8. 不要太肉麻（比如想你之类的，就日常聊天）
    伴侣性格：
        - %s
    你必须严格遵守上述规则来回复用户。
    """


# 统一响应类
class Result(BaseModel):
    code : int
    message : str
    data : Any = None


class RequestSessions(BaseModel):
    nature : str
    nick_name : str

# 会话类
class Sessions(BaseModel):
    nature : str
    nick_name : str

# ai对话模板
class RequestChat(BaseModel):
    session_name :str
    message : str
    nick_name : str
    nature : str


# 全局异常处理器
@app.exception_handler(Exception)
def exception_handler(request: Request, exc: Exception):
    logging.info(request.method)
    logging.info(request.url)
    logging.info(request.headers)
    logging.error(exc)
    return JSONResponse(
        content={"code": 500, "message": "服务端内部异常", "data": None}
    )

# 抽取获取会话与资源释放到方法
async def get_session():
    # 获取会话对象
    session = session_factory()
    try:
        yield session
    except Exception as e:
        logging.error(e)
        await session.rollback()
        raise
    finally:
        await session.close()


# 读取预设返回信息
@app.get("/api/presets")
async def get_presets(session: AsyncSession = Depends(get_session)):
    # 查询ai_preset表
    result = await session.execute(select(AiPreset).order_by(AiPreset.sort_order.asc()))
    # 获取到的数据进行json序列化
    preset_list = jsonable_encoder(result.scalars().all())
    # 返回结果给前端
    return Result(code=200, message="预设信息加载成功", data=preset_list)


# 创建会话
@app.post("/api/sessions")
async def create_sessions(sessions : RequestSessions, session: AsyncSession = Depends(get_session)):
    session_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    ai_session = AiSession(session_name=session_name, nick_name=sessions.nick_name, nature=sessions.nature,
                           create_time=datetime.now(), update_time=datetime.now())
    session.add(ai_session)
    # 提交修改
    await session.commit()

    # 3. 给前端响应
    return Result(code = 200, message = "创建会话成功", data = session_name)


# 删除会话
@app.delete("/api/sessions/{session_name}")
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
@app.get("/api/sessions")
async def get_sessions_list(session: AsyncSession = Depends(get_session)):
    logging.info("获取会话列表")
    session_result = await session.execute(select(AiSession.session_name)
                                           .order_by(AiSession.session_name.desc()))
    session_list = session_result.scalars().all()
    return Result(code=200, message="会话列表加载成功", data = session_list)


# 获取指定会话
@app.get("/api/sessions/{session_name}", summary="获取指定会话信息")
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


# 聊天功能
@app.post("/api/chat")
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

    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

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



# 启动服务
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="192.168.16.170", port=8000)



