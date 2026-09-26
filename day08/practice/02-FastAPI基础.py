from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    age: int
    gender: str


@app.get("/hello")
def hello_fastapi():
    print("Hello FastAPI!")
    return "ok"


@app.get("/users")
def hello_fastapi():
    print("获取用户信息中 . . .")
    return [
        User(name = "胡一菲", age = 27, gender = "female"),
        User(name = "曾小贤", age = 28, gender = "male"),
        User(name = "吕子乔", age = 26, gender = "male")
    ]


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="192.168.16.170", port=8000)