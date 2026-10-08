from typing import Any
from pydantic import BaseModel


# 业务Pydantic模型
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