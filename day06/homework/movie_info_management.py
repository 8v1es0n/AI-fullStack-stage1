"""
【电影信息管理系统需求说明】
1. 业务背景
   使用面向对象思想，开发一个电影信息管理系统，可对电影信息进行
   添加、修改、删除、精确查询、查询所有、查询评分最高等操作。

2. 涉及到的类
   2.1 Movie（电影类）
       - 实例属性：电影名(name)、导演(director)、主演(actor)、票价(price)、评分(score)
       - 方法：
           * __init__：初始化方法
           * __str__：返回电影的字符串表示，格式为：
             "电影名: xxx | 导演: xxx | 主演: xxx | 票价: xxx | 评分: xxx"
           * update_info：支持更新电影信息

   2.2 MovieSystem（电影信息管理系统类）
       - 类属性：system_name（系统名称）、system_version（系统版本号）
       - 实例属性：movie_list（用于存放所有电影对象的列表）
       - 方法：
           * __init__：初始化方法，创建一个空的 movie_list
           * add_movie：添加电影
           * update_movie：修改电影
           * delete_movie：删除电影
           * query_movie：精确查询指定电影
           * list_movies：展示所有电影
           * rank_movie_score：按照评分排行打印电影信息（若有并列，一并输出）
           * run：显示菜单并循环接收用户操作

3. 业务规则
   3.1 添加电影时：
       - 依次输入电影名、导演、主演、票价、评分
       - 电影名不能重复（已存在则提示并返回）
       - 票价必须大于 0，评分必须在 0-10 之间，否则提示并返回
   3.2 修改电影时：
       - 输入要修改的电影名
       - 若不存在则提示"未找到该电影"
       - 找到后依次输入新的导演、主演、票价、评分，并更新
   3.3 删除电影时：
       - 输入要删除的电影名
       - 若不存在则提示"未找到该电影"
   3.4 查询电影时：
       - 输入电影名进行精确查询
   3.5 按照评分排行打印电影信息：

4. 菜单
       1. 添加电影   2. 修改电影   3. 删除电影
       4. 查询指定电影  5. 查询所有电影
       6. 按照评分排行打印电影信息  7. 退出系统
"""


class Movie:
    def __init__(self, mov_name, mov_director, mov_actor, mov_price, mov_score):
        self.name = mov_name
        self.director = mov_director
        self.actor = mov_actor
        self.price = mov_price
        self.score = mov_score

    def __repr__(self):
        return (f'电影名为:{self.name}, 导演是: {self.director}, 主演为: {self.actor}, '
                f'电影票的价格: {self.price}, 电影评分: {self.score}')


class MovieSystem:
    system_name = "电影信息管理系统"
    system_version = "0.1.0"

    def __init__(self):
        self.movie_dict = {}

    # 添加电影
    def add_movie(self):
        name = input("请输入电影名: ")
        if name in self.movie_dict.keys():
            print("此电影信息已存在 . . .")
            return

        director = input("请输入电影的导演: ")
        actor = input("请输入电影的主演: ")
        price = float(input("请输入电影的票价: "))
        score = float(input("请输入电影的评分: "))
        if price >= 0 and 0 <= score <= 10:
            self.movie_dict[name] = Movie(name, director, actor, price, score)
            print("添加成功")
        else:
            print("输入有误 . . .")
            return

    # 修改电影
    def update_movie(self):
        name = input("请输入要修改的电影名: ")
        if name not in self.movie_dict.keys():
            print("此电影信息不存在 . . .")
            return

        director = input("请输入要修改电影的导演: ")
        actor = input("请输入要修改电影的主演: ")
        price = float(input("请输入要修改电影的票价: "))
        score = float(input("请输入要修改电影的评分: "))
        if price >= 0 and 0 <= score <= 10:
            self.movie_dict[name] = Movie(name, director, actor, price, score)
            print("修改成功")
        else:
            print("输入有误 . . .")

    # 删除电影
    def delete_movie(self):
        name = input("请输入要删除的电影名: ")
        if name not in self.movie_dict.keys():
            print("此电影信息不存在 . . .")
            return

        self.movie_dict.pop(name)
        print("删除成功")

    # 精准查询
    def query_movie(self):
        name = input("请输入要查找的电影名: ")
        if name not in self.movie_dict.keys():
            print("此电影信息不存在 . . .")
            return

        movie_info = self.movie_dict[name]
        print(f"电影当前的信息为{movie_info}")

    # 展示所有电影
    def list_movies(self):
        if len(self.movie_dict) == 0:
            print("暂无电影信息 . . .")
        else:
            movies = self.movie_dict.values()
            for movie in movies:
                print(movie)
            print("查询成功")

    # 评分排行
    def rank_movie_score(self):
        if len(self.movie_dict) == 0:
            print("暂无电影信息 . . .")
        else:
            sorted_movies = sorted(self.movie_dict.values(),
                                   key = lambda m: m.score, reverse = True)

            for movie in sorted_movies:
                print(movie)

    # 程序运行入口
    def run(self):
        print(f"欢迎使用{MovieSystem.system_name} V{MovieSystem.system_version}")

        while True:
            print()
            print(
                "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print(
                "# 1.添加电影  2.修改电影  3.删除电影  4.查询指定电影  5.查询所有电影  6.查询评分排行  7.退出系统 #")
            print(
                "# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()

            choice = input("请选择要执行的操作, 输入1-7: ")

            try:
                match choice:
                    case "1":  # 添加电影
                        self.add_movie()
                    case "2":  # 修改电影
                        self.update_movie()
                    case "3":  # 删除电影
                        self.delete_movie()
                    case "4":  # 查询指定电影
                        self.query_movie()
                    case "5":  # 查询所有电影
                        self.list_movies()
                    case "6":  # 查询评分最高电影
                        self.rank_movie_score()
                    case "7":  # 退出系统
                        print("Bye ~")
                        break
                    case _:  # 其他情况
                        print("输入错误, 请选择1-7之间的菜单功能!")
            except ValueError:
                print("输入的数据有问题, 请检查, 然后重新输入 !!!")
            except Exception:
                print("程序运行出错了, 请重新选择 ~")

    # ================================================================================
    # 主入口：选择要运行的作业题
    # ================================================================================


if __name__ == '__main__':
    # BookSystem().run()

    MovieSystem().run()
