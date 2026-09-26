"""
==========================================================
作业: 基于 FastAPI 开发"图书信息查询"API接口
==========================================================

【作业需求】
    使用 FastAPI 框架, 开发一个简单的"图书馆图书信息查询"API接口服务,
    用于查询图书馆中的图书列表信息。

【具体要求】
    1. 创建一个 FastAPI 实例对象, 并指定:
       - title       = "图书信息查询系统"
       - description = "一个简单的图书馆图书信息查询API"
       - version     = "0.1.0"
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="图书信息查询系统",
    description="一个简单的图书馆图书信息查询API",
    version="0.1.0"
)

"""
    2. 使用 Pydantic 模型定义图书数据结构 (类名: Book), 包含以下字段:
       - id      : int   图书ID
       - name    : str   图书名称
       - author  : str   作者
       - price   : float 价格
       - stock   : int   库存数量
"""

class Book(BaseModel):
    id: int
    name: str
    author: str
    price: float
    stock: int

all_book = [
        Book(id = 1001, name= "白雪公主", author= "白雪", price= 33.00, stock= 99),
        Book(id = 1001, name= "哈利波特", author= "那多", price= 45.90, stock= 80),
        Book(id = 1001, name= "查理九世", author= "凯尔", price= 23.70, stock= 36),
        Book(id = 1001, name= "福尔摩斯", author= "查理", price= 66.77, stock= 54)
    ]

"""
    3. 开发以下 3 个 API 接口:
       (1) GET /
           - 功能: 根路径, 返回欢迎信息
           - 返回: {"message": "欢迎使用图书信息查询系统!"}

       (2) GET /books
           - 功能: 获取所有图书列表
           - summary: "获取所有图书列表"
           - response_model: list[Book]
           - 返回: 至少包含 3 本图书信息的列表, 图形信息定义在代码中即可
           - 提示: 在控制台打印 "获取图书列表..."

       (3) GET /books/count
           - 功能: 获取图书总数量
           - summary: "获取图书总数"
           - 返回: {"total": 图书数量}
"""

@app.get("/", summary="欢迎页")
def root():
    return {"message": "欢迎使用图书信息查询系统!"}

@app.get("/books", summary="获取所有图书列表", response_model=list[Book])
def get_books():
    print("图书列表查询中 . . .")
    return

@app.get("/books/count", summary="获取图书总数及总库存")
def get_books_count():
    print("图书总量获取中 . . .")
    stock = 0
    for book in all_book:
        stock += book.stock
    return f"图书数为: {len(all_book)}, 总库存为: {stock}"

"""
    4. 通过代码方式启动 FastAPI 服务
       - host = "0.0.0.0"
       - port = 8000

    5. 启动后测试:
       - 在浏览器访问 http://localhost:8000/                   访问首页
       - 在浏览器访问 http://localhost:8000/books              查看图书列表
       - 在浏览器访问 http://localhost:8000/books/count        查看图书数量
       - 在浏览器访问 http://localhost:8000/docs               查看自动生成的接口文档
==========================================================
"""
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)