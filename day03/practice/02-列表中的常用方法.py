"""
方法                          作用                          样例                  备注
append()                在列表的尾部追加元素              s.append(10086)
insert()                在指定索引之前，插入该元素         s.insert(0, 92)
remove()                移除列表中第一个匹配到的值         s.remove(75)
pop()                   删除列表中指定索引位置的元素       s.pop(2) / s.pop()       如果未指定索引，默认删最后一个
sort()                  对列表进行排序                    s.sort()                列表元素的数据类型一致，才可以进行排序
reverse()               反转列表元素                      s.reverse()
"""
from os import remove

list01 = ["貂蝉", "大乔", "小乔", "孙尚香", "甄姬"]
list02 = [4, 8, 1, 4, 9, 5, 6]

# append()  在列表的尾部追加元素
list01.append("黄月英")

# insert()  在指定索引之前，插入该元素
list01.insert(1, "马云禄")

# remove()  移除列表中第一个匹配到的值
list01.remove("小乔") #删除的必须是列表中有的, 否则报错

# pop() 删除列表中指定索引位置的元素
list01.pop(1)
list01.pop()    # 如果未指定索引，默认删最后一个

# sort()    对列表进行排序
# 列表元素的数据类型一致，才可以进行排序
list02.sort()   # 升序
list02.sort(reverse=True)   # 降序

# reverse()   反转列表元素
list02.reverse()

# 方法存在返回值
# 复制调用
count = list02.count(3)
print(count)

# 输出调用
print(list02.count(3))