wuxia_couples = {
    "郭靖": "黄蓉",
    "杨过": "小龙女",
    "张无忌": "赵敏",
    "令狐冲": "任盈盈",
    "萧峰": "阿朱",
    "段誉": "王语嫣",
    "虚竹": "梦姑",
    "袁承志": "温青青",
    "陈家洛": "霍青桐",
    "韦小宝": "建宁公主"
}

# 增加    键不存在
wuxia_couples["李逍遥"] = "赵灵儿"

# 修改    键存在
wuxia_couples["虚竹"] = "西夏公主"

# 删除
wuxia_couples.pop("韦小宝")

# 查询
wuxia_couples.get("杨过")

items = wuxia_couples.items()
print(items)

# 遍历字典
for key, val in wuxia_couples.items():
    print(dik, diy)