__all__ = ["PI" , "log_separator2"]

# 常量(不会发生变化的数据 ; 常量的名称为全部大写)
PI = 3.1415926
NAME = "黑马程序员"

# 函数
def log_separator1():
    print("- " * 30) # "- "重复输出30次

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

# print(__name__) # __main__

if __name__ == "__main__":
    log_separator2()
    log_separator3()
    log_separator4()