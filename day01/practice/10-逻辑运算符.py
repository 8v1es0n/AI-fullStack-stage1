a = 10
b = 20
c = 10

print("-------------")

print(a > b and b > c) #  False and True =  False
print(a < b and b > c) #  True  and True =  True
print(a > b and b < c) #  False and False = False
# Simplify chained comparison (简化比较连接)
print(a < b < c) #  True  and False = False

print("-------------")

print(a > b or b > c) #  False or True =  True
print(a < b or b > c) #  True  or True =  True
print(a > b or b < c) #  False or False = False
print(a < b or b < c) #  True  or False = True

print("-------------")

print(not(a > b))