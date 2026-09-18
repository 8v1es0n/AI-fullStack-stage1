# set集合 : 无序(存取顺序不一致叫做无序) , 元素唯一 , 元素可以修改

# 定义方式
set01 = {"a", "c", "d", "e"}

# 定义空的set集合
# set02 = set()
# print(type(set02))


# add(..)	        添加元素到集合中	s1.add('t')
# set01.add(100)

# remove(..)	    移除集合中的指定元素（指定元素不存在将报错）	s1.remove('t')
# set01.remove(3)

# pop()	            随机删除集合中的元素并返回	e = s1.pop()
# set01.pop()

# clear()	        清空集合	s1.clear()
# set01.clear()


set001 = {1, 2, 3, 4}
set002 = {2, 3, 5, 6}

# difference()	    求取两个集合的差集（第一个集合里有、但第二个集合里没有的）	s1.difference(s2)
print(set001.difference(set002))
# union()	        求取两个集合的并集	s1.union(s2)
print(set001.union(set002))
# intersection()	求取两个集合的交集	s1.intersection(s2)
print(set001.intersection(set002))

# 不能根据索引修改
# set01[3] = 100

print(set01)
