# SQLAlchemy引擎、会话工厂、Base基类、获取会话对象
import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

# 1. 创建引擎(支持异步操作)
engine = create_async_engine("mysql+aiomysql://root:1234@localhost:3306/mydb?charset=utf8mb4", echo=True)

# 2. 声明模型类
class Base(DeclarativeBase):
    pass

# 3. 会话工厂(支持异步操作)
session_factory = async_sessionmaker(engine)

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