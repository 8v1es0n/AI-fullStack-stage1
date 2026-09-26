from day07.practice import *


class LibrarySystem:
    def __init__(self):
        # 所有的图书信息 , 类型属于字典  键:书的编号  值:书的对象
        self.books = {
            "1001": mod_book.Book("1001", "《Python 教程》", "张三", 5),
            "1002": mod_book.Book("1002", "《C++ 教程》", "李四", 3),
            "1003": mod_book.Book("1003", "《Java 教程》", "王五", 2),
            "1004": mod_book.Book("1004", "《C 教程》", "赵六", 1),
            "1005": mod_book.Book("1005", "《JavaScript 教程》", "田七", 4)
        }

        # 所有的会员信息  , 类型属于字典  键:会员的卡号  值: 会员对象
        self.members = {
            "N001": mod_member.NormalMember("N001", "张三", "668001"),
            "N002": mod_member.NormalMember("N002", "李四", "668002"),
            "N003": mod_member.NormalMember("N003", "王五", "668003"),
            "V001": mod_member.VIPMember("V001", "赵六", "669001", 1),
            "V002": mod_member.VIPMember("V002", "孙七", "669002", 2),
            "V003": mod_member.VIPMember("V003", "周八", "669003", 3),
            "V004": mod_member.VIPMember("V004", "吴九", "669004", 4)
        }
        # 当前登录会员 , 当登录成功给属性赋值
        self.current_member: mod_member.Member | None = None


    def login(self):
        print("[登录]")
        while True:
            member_id = input("请输入会员卡号:")

            if member_id in self.members.keys():
                # 卡号存在 , 判断密码
                pwd = input("请输入会员密码:")

                # 根据卡号获取 登录的用户对象
                member = self.members.get(member_id)
                if member.get_password() == pwd:
                    print(f"欢迎 {member.name} 进入系统!")
                    self.current_member = member
                    print("登录成功~")
                    return True
                else:
                    print("登录失败,您输入的密码有误!")
                    continue
            else:
                print("当前输入的卡号不存在,请重新输入...")
                continue


    def handle_borrow_book(self):       # 借书
        # 获取图书馆的所有书对象容器
        print("所有的图书信息如下: ")
        for book in self.books.values():
            # 打印内容 , 因为Book类生成了魔法方法 repr
            print(book)

        book_id = input("请输入借阅图书的编号: ")
        if book_id in self.books.keys():
            self.current_member.borrow_book(self.books[book_id])
            print("借阅成功~")
        else:
            print("您输入的图书编号不存在!")
            return


    def handle_return_book(self):       # 还书
        # 1. 显示所有已借阅的图书信息
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("您已借阅的图书信息如下: ")
            for book in borrowed_books:
                print(f"编号: {book.book_id}, 书名: {book.title}")
        else:
            print("您没有任何的借阅记录!")

        # 2. 输入图书编号, 执行还书操作
        book_id = input("请输入图书的编号: ")
        for book in borrowed_books:
            if book.book_id == book_id:
                self.current_member.return_book(book)
                print("还书成功~")
                return
        print("您输入的编号有误!")


    def show_borrowed_books(self):      # 查看我的借阅
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("您已借阅的图书信息如下: ")
            for book in borrowed_books:
                print(f"编号: {book.book_id}, 书名: {book.title}")
        else:
            print("您没有任何的借阅记录!")


    def run(self):  # 运行系统
        if self.login():
            while True:
                print("\n1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看借阅")
                print("4. 退出系统")

                choice = input("请选择操作(1-4): ")
                match choice:
                    case "1":
                        self.handle_borrow_book()
                    case "2":
                        self.handle_return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统, Bye Bye ~")
                        break
                    case _:
                        print("无效的选项，请重新选择！")



if __name__ == '__main__':
    LibrarySystem().run()