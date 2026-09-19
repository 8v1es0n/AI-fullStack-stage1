
"""
    案例:
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。
    系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
    具体功能如下：
        1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
        5. 退出购物车

    结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""
shopping_cart = {}
menu = """
########### 购物车系统 ##########
#         1. 添加购物车         #
#         2. 修改购物车         #
#         3. 删除购物车         #
#         4. 查询购物车         #
#         5. 退出购物车         #
###############################
"""
print("欢迎使用购物车管理系统 ~")

while True:
    # 1. 制作菜单
    print(menu)

    # 2. 执行的具体操作
    choice = input("请选择要执行的操作(1-5): ")
    goods_len = len(shopping_cart)
    match choice:
        case "1":  # 添加购物车
            # 输入信息
            while True:
                goods_name = input("请输入要添加的商品名称: ")
                if goods_name in shopping_cart.keys():
                    print("商品已存在于购物车, 请重新输入. . .")
                    continue
                else:
                    break
            goods_price = float(input("请输入商品价格: "))
            goods_num = int(input("请输入商品数量: "))
            shopping_cart[goods_name] = {"goods_price": goods_price, "goods_num": goods_num}
            print(f"商品 {goods_name} 已成功添加到购物车")

        case "2":  # 修改购物车
            if goods_len == 0:
                print("购物车为空, 无法完成修改操作")
                continue
            while True:
                goods_name = input("请输入要修改的商品名称: ")
                if goods_name not in shopping_cart:
                    print("商品不存在于购物车, 无法完成修改, 请重新输入. . .")
                    continue
                else:
                    break
            goods_price = float(input("请输入商品价格: "))
            goods_num = int(input("请输入商品数量: "))
            shopping_cart[goods_name] = {"goods_price": goods_price, "goods_num": goods_num}
            print(f"商品 {goods_name} 已成功修改")

        case "3":  # 删除购物车
            if goods_len == 0:
                print("购物车为空, 无法完成删除操作")
                continue
            while True:
                goods_name = input("请输入要删除的商品名称: ")
                if goods_name not in shopping_cart:
                    print("商品不存在于购物车, 无法完成删除, 请重新输入. . .")
                    continue
                else:
                    break
            shopping_cart.pop(goods_name)
            print(f"商品 {goods_name} 已成功删除")

        case "4":  # 查询购物车
            if goods_len == 0:
                print("购物车为空, 无法完成查询操作")
                continue
            while True:
                goods_name = input("请输入要查询的商品名称: ")
                if goods_name not in shopping_cart:
                    print("商品不存在于购物车, 无法查询, 请重新输入. . .")
                    continue
                else:
                    break
            for key, val in shopping_cart.items():
                print(f"商品 {goods_name} 的价格为: {val["goods_price"]} 数量为: {val['goods_num']}")

        case "5":  # 退出购物车
            print("期待您的下次使用 ~")
            break
        case _:  # 匹配其他所有情况
            print("非法操作, 请重新输入. . .")