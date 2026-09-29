from datetime import datetime
import json
import os
from typing import Any

from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel
import logging
from fastapi import Request
from starlette.responses import JSONResponse

# 配置日志
logging.basicConfig(

    # 日志级别
    level=logging.INFO,
    # 日志输出格式
    format = "%(asctime)s - %(levelname)s - [%(filename)s : %(lineno)d] - %(message)s"
)



app = FastAPI()
# 加载人设
COMPANION_PRESETS_PATH = "./frontend/data/companion_presets.json"

# 会话文件路径
SESSION_DRI = "frontend/session"

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

# 判断会话文件夹是否存在
if not os.path.exists(SESSION_DRI):
    os.mkdir(SESSION_DRI)

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

# 读取预设返回信息
@app.get("/api/presets")
async def get_presets():

    # 1 读取人设文件中的数据
    # 1.1 人设文件不存在,给出提示
    if os.path.exists(COMPANION_PRESETS_PATH):
        with open(COMPANION_PRESETS_PATH, "r", encoding="utf-8") as f:
            preset_list = json.load(f)
            preset_list.sort(key=lambda preset: preset["sort_order"])
        return Result(code=200, message = "预设信息加载成功", data=preset_list)
    else:
        return Result(code = 404, message = "预设数据资源不存在", data = None)


# 创建会话
@app.post("/api/sessions")
async def create_sessions(sessions : RequestSessions):
    # 1. 组织存储的内容
    # 会话名字,当前时间
    session_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    session_dict = {
        "session_name" : session_name,
        "nick_name" : sessions.nick_name,
        "nature" : sessions.nature,
        "messages" : []
    }

    # 2. 把组织好的数据写进文件
    with open(f"{SESSION_DRI}/{session_name}.json", "w", encoding="utf-8") as f:
        json.dump(session_dict, f, ensure_ascii = False, indent = 4)

    # 3. 给前端响应
    return Result(code = 200, message = "创建会话成功", data = session_name)


# 删除会话
@app.delete("/api/sessions/{session_name}")
async def delete_sessions(session_name : str):
    if not os.path.exists(f"{SESSION_DRI}/{session_name}.json"):
        return Result(code=404, message="未找到会话信息", data=None)

    # 删除会话文件
    os.remove(f"{SESSION_DRI}/{session_name}.json")

    # 3. 给前端响应
    return Result(code = 200, message = "删除会话成功", data = None)

# 获取会话列表
@app.get("/api/sessions")
async def get_sessions_list():
    logging.info("获取会话列表")
    if not os.path.exists(SESSION_DRI) or len(os.listdir(SESSION_DRI)) == 0:
        return Result(code=404, message="会话列表为空", data = None)

    session_list = []
    for name in os.listdir(SESSION_DRI):
        if name.endswith(".json"):
            # 获取文件名,并存到列表中
            name = name.rstrip(".json")
            session_list.append(name)
    # 降序排序
    session_list.sort(reverse=True)
    return Result(code=200, message="会话列表加载成功", data = session_list)


# 获取指定会话
@app.get("/api/sessions/{session_name}", summary="获取指定会话信息")
async def get_sessions_byid(session_name : str):
    if not os.path.exists(f"{SESSION_DRI}/{session_name}.json"):
        return Result(code=404, message="未找到会话信息", data=None)

    # 读取文件
    with open(f"{SESSION_DRI}/{session_name}.json", "r", encoding="utf-8") as f:
        session_data = json.load(f)
        return Result(code = 200, message = "加载会话成功", data = session_data)


# 聊天功能
@app.post("/api/chat")
async def ai_chat(chat : RequestChat):
    # 1. 从文件中读取会话
    with open(f"{SESSION_DRI}/{chat.session_name}.json", "r", encoding="utf-8") as f:
        # 加载所有记录
        chat_dict = json.load(f)

        history_list = chat_dict["messages"]

    # 组织角色信息
    if len(history_list) == 0:
        history_list.append({"role": "system", "content": SYSTEM_PROMPT_TEMPLATE % (chat.nick_name, chat.nature)})
    else:
        history_list[0] = {"role": "system", "content": SYSTEM_PROMPT_TEMPLATE % (chat.nick_name, chat.nature)}
    history_list.append({"role": "user", "content": chat.message})

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

    history_list.append({"role": "assistant", "content":assistant})
    chat_dict["messages"] = history_list
    chat_dict["nick_name"] = chat.nick_name
    chat_dict["nature"] = chat.nature

    with open(f"{SESSION_DRI}/{chat.session_name}.json","w",encoding="utf-8") as f:
        json.dump(chat_dict,f,ensure_ascii=False,indent=4)
    return Result(code = 200, message = "对话信息返回成功", data=assistant)

    # 启动FastAPi服务
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="192.168.16.170", port=8000)



