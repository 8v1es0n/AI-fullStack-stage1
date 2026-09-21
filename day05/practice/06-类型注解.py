# 变量 和 数据容器的 类型注解
a: int = 1.1
b: str = "abc"
c: bool = True
d: None = None

# 类型注解 , 标明当前变量的类型属于int类型 , 如果给出其他类型会有黄色警告 , 但是可以正常使用!
print(a)

# 列表
list01: list[int | str] = [1, 2, 3, 4, 5, "a"]

# 元组 : 元组的长度是固定的
tuple01: tuple[int | str, ...] = (1, 2, 3, "a")

# 集合
set01: set[int | str] = {1, 2, 3, 4, 5, "a"}

# 字典
dict01: dict[str, int | str] = {"name": "杨幂", "age": 10}


def max_min(list01: list[int]) -> tuple[int, ...]:
    max_value = max(list01)
    min_value = min(list01)
    return max_value, min_value


print(max_min([1, 2, 3, 4, 5]))
