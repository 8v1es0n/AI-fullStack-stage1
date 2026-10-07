from datetime import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, select, or_, update, delete
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


# 创建SQLAlchemy引擎, 管理数据库连接与配置
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/mydb", echo=False)


# 声明模型的基类
class DeclBase(DeclarativeBase):
    pass

 # 定义类与表的映射关系
class AiMessage(DeclBase):
    __tablename__ = "ai_message"

    # 属性映射字段
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, comment='主键')
    session_id: Mapped[int] = mapped_column(Integer, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    content: Mapped[str] = mapped_column(String(500), nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    def __repr__(self):
        return f"<AiMessage(id={self.id}, session_id={self.session_id}, role={self.role}, content={self.content}, create_time={self.create_time})>"


# 新增
# if __name__ == '__main__':
#     # 获取操作数据库的会话对象session
#     session = Session(engine)
#
#     # 执行操作
#     session.add(AiMessage(session_id=1, role="user", content="你笑什么呢~", create_time=datetime.now()))
#     session.add(AiMessage(session_id=1, role="assistant", content="就是好笑呀", create_time=datetime.now()))
#     # 提交事务
#     session.commit()
#
#     # 释放session
#     session.close()


# 查询
# if __name__ == '__main__':
#     # with 上下文管理器, 用完自动释放资源
#     # 获取会话对象
#     with Session(engine) as session:
#         # 查询所有字段
#         message__all = session.execute(select(AiMessage)).all()
#         # 返回的数据类型属于list列表
#         for message in message__all:
#             print(message[0])


# 查询指定字段
# if __name__ == '__main__':
#     # with 上下文管理器, 用完自动释放资源
#     # 获取会话对象
#     with Session(engine) as session:
#         # 查询所有字段
#         message__all = session.execute(select(AiMessage.id, AiMessage.role, AiMessage.content)).all()
#         # 返回的数据类型属于list列表
#         for message in message__all:
#             print(message[0])


# 条件查询
# if __name__ == '__main__':
#     # with 上下文管理器, 用完自动释放资源
#     # 获取会话对象
#     with Session(engine) as session:
#         # 返回单条数据
#         result = session.execute(select(AiMessage).where(AiMessage.id == 7)).scalars().one()
#         # 返回的数据类型属于list列表
#         print(result)
#         print("-" * 20)
#
#         # 同时满足多个条件
#         result_list1 = session.execute(select(AiMessage)
#                                   .where(AiMessage.content.like("%你%"), AiMessage.role == "user")).scalars().all()
#         # 返回的数据类型属于list列表
#         for result in result_list1:
#             print(result_list1)
#         print("-" * 20)
#
#         # 满足任一条件
#         result_list2 = session.execute(select(AiMessage)
#                                   .where(or_(AiMessage.content.like("%你%"),
#                                              AiMessage.role == "user"))).scalars().all()
#         # 返回的数据类型属于list列表
#         for result in result_list2:
#             print(result_list2)


# 排序查询
# if __name__ == '__main__':
#     with Session(engine) as session:
#         message_list1 = session.execute(select(AiMessage)
#                                   .where(AiMessage.content.like("%你%"), AiMessage.role == "user")
#                                   .order_by(AiMessage.create_time.desc(), AiMessage.id.asc())).scalars().all()
#         # 返回的数据类型属于list列表
#         for result in message_list1:
#             print(message_list1)


# 分页查询
# if __name__ == '__main__':
#     with Session(engine) as session:
#         results = session.execute(
#             select(AiMessage).where(or_(AiMessage.session_id == 1, AiMessage.role == 'user'))
#             .offset(4).limit(2)).scalars().all()
#         for message in results:
#             print(message)


# 修改操作
# if __name__ == '__main__':
#     with Session(engine) as session:
#         session.execute(update(AiMessage)
#                         .where(AiMessage.id == 1).values(content="你好", create_time=datetime.now()))
#
#         session.commit()


# 删除数据
# if __name__ == '__main__':
#     with Session(engine) as session:
#         # 6. 删除操作 --> 需求: 删除id为10的数据
#         session.execute(delete(AiMessage).where(AiMessage.id == 5))
#         session.execute(delete(AiMessage).where(AiMessage.id.in_([6, 7, 8])))
#         session.commit()