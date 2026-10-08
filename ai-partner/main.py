from fastapi import FastAPI

import logging
from fastapi import Request

from starlette.responses import JSONResponse

from app.routers import *


# 配置日志
logging.basicConfig(
    # 日志级别
    level=logging.INFO,
    # 日志输出格式
    format = "%(asctime)s - %(levelname)s - [%(filename)s : %(lineno)d] - %(message)s"
)



app = FastAPI()

app.include_router(preset_router)
app.include_router(session_router)
app.include_router(chat_router)


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




# 启动服务
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="192.168.16.170", port=8000)