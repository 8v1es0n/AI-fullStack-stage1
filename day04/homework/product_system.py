"""
    案例：商品管理系统
    1. 添加商品信息：根据提示录入商品名称、分类、价格、库存数量，录入完成保存到系统中。
    2. 修改商品信息：输入要修改的商品名称，然后再提示输入新的分类、价格、库存数量，输入完成后修改商品信息。
    3. 删除商品信息：输入要删除的商品名称，根据名称删除商品信息。
    4. 查询商品信息：输入要查询的商品名称，根据名称查询商品信息并输出。
       为空则列出所有商品：遍历所有商品信息并输出。
    6. 商品统计：统计商品总数、库存总量、总价值、价格最高和最低的商品信息。
    7. 退出系统。
"""

menu = """
# # # # # # # # # # # # # # # # # # # # # # # 【商品管理 系统菜单】 # # # # # # # # # # # # # # # # # # # #
#       1. 添加商品  2. 修改商品  3. 删除商品  4. 查询商品(" "查询所有商品)   5. 统计班级成绩   6. 退出系统   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用商品管理系统 ~")

# 定义一个字典
products = {}

while True:
    print(menu)
    choice = input("请选择要执行的操作(1-6): ")

    # 根据输入的序号,进入不同分支
    match choice:
        # 1. 添加商品信息：根据提示录入商品名称、
        # 分类、价格、库存数量，录入完成保存到系统中。
        case "1":
            while True:
                product_name = input("请输入要添加的商品名称: ")
                if product_name in products.keys():
                    print(f"{product_name} 的信息已存在于系统中, 请重新输入 . . .")
                    continue
                else:
                    break
            prod_type = input("请输入商品分类: ")
            price = float(input("请输入商品价格: "))
            inventory = int(input("请输入库存数量: "))
            products[product_name] = {"prod_type": prod_type, "price": price,
                                            "inventory": inventory}
            print(f"{product_name} 的商品信息已添加成功")

        # 2. 修改商品信息：要求输入要修改的商品名称，
        # 然后再提示输入分类、价格、库存，输入完成后修改商品信息。
        case "2":
            while True:
                product_name = input("请输入要修改的商品名称: ")
                if product_name not in products.keys():
                    print(f"{product_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    break
            prod_type = input("请输入分类: ")
            price = float(input("请输入价格: "))
            inventory = int(input("请输入库存: "))
            products[product_name] = {"prod_type": prod_type, "price": price,
                                            "inventory": inventory}
            print(f"{product_name} 的商品信息已修改成功")

        # 3. 删除商品信息：要求输入要删除的商品名称，根据名称删除商品信息。
        case "3":
            while True:
                product_name = input("请输入要删除的商品名称: ")
                if product_name not in products.keys():
                    print(f"{product_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    break
            products.pop(product_name)
            print(f"{product_name} 的商品信息已删除成功")


        # 4. 查询商品信息：要求输入要查询的商品名称，根据名称查询商品信息并输出。
        #    为空则列出所有商品：遍历所有商品信息并输出。
        case "4":
            while True:
                product_name = input("请输入要查询的商品名称: ")
                if product_name == " ":
                    for product, info in products.items():
                        print(f"商品: {product_name} 的 分类为: {info["prod_type"]} "
                              f"价格为: {info["price"]} 库存为: {info["inventory"]}")
                    break

                elif product_name not in products.keys():
                    print(f"{product_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    # 单独查询一本商品
                    for product, info in products.items():
                        if product == product_name:
                            print(f"商品: {product_name} 的 分类为: {info["prod_type"]} "
                                  f"价格为: {info["price"]} 库存为: {info["inventory"]}")
                            print(f"{product_name} 的商品信息已查询成功")
                    break

        case "5":
            # 5. 商品统计：统计商品总数、库存总量、总价值、价格最高和最低的商品信息。
            print(f"商品总量为: {len(products)}")

            # all_inventory = 0
            # inventory_list = [info["inventory"] for info in products.values())]
            # for num in inventory_list:
            #     all_inventory += num
            # print(f"库存总量为: {all_inventory}")

            all_inventory = sum(info["inventory"] for info in products.values())
            print(f"库存总量为: {all_inventory}")

            all_value = 0.0
            for info in products.values():
                all_value += info["price"] * info["inventory"]
            print(f"总价值为: {all_value}")

            price_list = [info["price"] for info in products.values()]

            max_price = max(price_list)
            min_price = max(price_list)
            sum_price = sum(price_list)
            print(f"最高的价格为: {max_price}")
            print(f"最低的价格为: {min_price}")
            print(f"平均价格为: {(sum_price / len(price_list)):.2f}")

            # 以及分类、价格、库存最高分和最低分的商品名称
            for name, info in products.items():
                if info["price"] == max_price:
                    print(f"价格最高的书名为: {name} 商品信息为: {info}")
                if info["price"] == min_price:
                    print(f"价格最低的书名为: {name} 商品信息为: {info}")

        # 6. 退出系统。
        case "6" | "ESC" | "Esc" | "esc":
            print("感谢您的使用, 希望与你下再次相遇!")
            break
        case _:
            print("输入错误")