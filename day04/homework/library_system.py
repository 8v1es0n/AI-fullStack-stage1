"""
    案例：图书管理系统
    1. 添加图书信息：根据提示录入图书名称、作者、价格、库存数量，录入完成保存到系统中。
    2. 修改图书信息：输入要修改的图书名称，然后再提示输入新的作者、价格、库存数量，输入完成后修改图书信息。
    3. 删除图书信息：输入要删除的图书名称，根据名称删除图书信息。
    4. 查询图书信息：输入要查询的图书名称，根据名称查询图书信息并输出。
       为空则列出所有图书：遍历所有图书信息并输出。
    5. 图书统计：统计图书总数、库存总量、总价值、价格最高和最低的图书信息。
    6. 退出系统。
"""

menu = """
# # # # # # # # # # # # # # # # # # # # # # # 【图书管理 系统菜单】 # # # # # # # # # # # # # # # # # # # #
#       1. 添加图书  2. 修改图书  3. 删除图书  4. 查询图书(" "查询所有图书)   5. 统计班级成绩   6. 退出系统   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用图书管理系统 ~")

# 定义一个字典
books = {}

while True:
    print(menu)
    choice = input("请选择要执行的操作(1-6): ")

    # 根据输入的序号,进入不同分支
    match choice:
        # 1. 添加图书信息：根据提示录入图书名称、
        # 作者、价格、库存数量，录入完成保存到系统中。
        case "1":
            while True:
                book_name = input("请输入要添加的图书名称: ")
                if book_name in books.keys():
                    print(f"{book_name} 的信息已存在于系统中, 请重新输入 . . .")
                    continue
                else:
                    break
            author = input("请输入图书作者: ")
            price = float(input("请输入图书价格: "))
            inventory = int(input("请输入库存数量: "))
            books[book_name] = {"author": author, "price": price,
                                            "inventory": inventory}
            print(f"{book_name} 的图书信息已添加成功")

        # 2. 修改图书信息：要求输入要修改的图书名称，
        # 然后再提示输入作者、价格、库存，输入完成后修改图书信息。
        case "2":
            while True:
                book_name = input("请输入要修改的图书名称: ")
                if book_name not in books.keys():
                    print(f"{book_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    break
            author = input("请输入作者: ")
            price = float(input("请输入价格: "))
            inventory = int(input("请输入库存: "))
            books[book_name] = {"author": author, "price": price,
                                            "inventory": inventory}
            print(f"{book_name} 的图书信息已修改成功")

        # 3. 删除图书信息：要求输入要删除的图书名称，根据名称删除图书信息。
        case "3":
            while True:
                book_name = input("请输入要删除的图书名称: ")
                if book_name not in books.keys():
                    print(f"{book_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    break
            books.pop(book_name)
            print(f"{book_name} 的图书信息已删除成功")


        # 4. 查询图书信息：要求输入要查询的图书名称，根据名称查询图书信息并输出。
        #    为空则列出所有图书：遍历所有图书信息并输出。
        case "4":
            while True:
                book_name = input("请输入要查询的图书名称: ")
                if book_name == " ":
                    for book, info in books.items():
                        print(f"图书: {book_name} 的 作者为: {info["author"]} "
                              f"价格为: {info["price"]} 库存为: {info["inventory"]}")
                    break

                elif book_name not in books.keys():
                    print(f"{book_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    # 单独查询一本图书
                    for book, info in books.items():
                        if book == book_name:
                            print(f"图书: {book_name} 的 作者为: {info["author"]} "
                                  f"价格为: {info["price"]} 库存为: {info["inventory"]}")
                            print(f"{book_name} 的图书信息已查询成功")
                    break

        case "5":
            # 5. 图书统计：统计图书总数、库存总量、总价值、价格最高和最低的图书信息。
            print(f"图书总量为: {len(books)}")

            # all_inventory = 0
            # inventory_list = [info["inventory"] for info in books.values()]
            # for num in inventory_list:
            #     all_inventory += num
            # print(f"库存总量为: {all_inventory}")

            all_inventory = sum(info["inventory"] for info in books.values())
            for nama, info in books.items():
                all_inventory += info["inventory"]
                # print(info["inventory"])
                # print(type(info["inventory"]))
            print(f"库存总量为: {all_inventory}")

            all_value = 0.0
            for info in books.values():
                all_value += info["price"] * info["inventory"]
            print(f"总价值为: {all_value}")

            price_list = [info["price"] for info in books.values()]

            max_price = max(price_list)
            min_price = max(price_list)
            sum_price = sum(price_list)
            print(f"最高的价格为: {max_price}")
            print(f"最低的价格为: {min_price}")
            print(f"平均价格为: {(sum_price / len(price_list)):.2f}")

            # 以及作者、价格、库存最高分和最低分的图书信息
            for name, info in books.items():
                if info["price"] == max_price:
                    print(f"价格最高的书名为: {name} 图书信息为: {info}")
                if info["price"] == min_price:
                    print(f"价格最低的书名为: {name} 图书信息为: {info}")

        # 6. 退出系统。
        case "6" | "ESC" | "Esc" | "esc":
            print("感谢您的使用, 希望与你下再次相遇!")
            break
        case _:
            print("输入错误")