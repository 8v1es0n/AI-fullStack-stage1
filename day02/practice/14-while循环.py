"""
# while语法结构

while 条件表达式:
    循环体语句1
    循环体语句2
    ......
else: (可选)
    条件为False，循环正常结束时执行
"""

# while 循环 : 打印10遍 "人生苦短, 我用Python~"
#  定义循环变量
i = 0
while i < 10:
    print("人生苦短, 我用Python~")
    i += 1
else:
    print("循环正常结束")

#  打印 1 ~ 100 之间所有的偶数(循环写法)
count = 1
while count < 101:
    if count % 2 == 0:
        print(count)
    count += 1

# 优化写法
count = 2
while count < 101:
    count += 2

# 需求：计算1-100之间所有偶数的累加之和
num = 1
sum = 0
while num < 101:
    if num % 2 == 0:
        sum += num
    num += 1
print(f"1-100之间所有偶数的累加之和为: {sum}")