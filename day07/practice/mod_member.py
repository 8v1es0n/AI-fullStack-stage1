from abc import ABC, abstractmethod

from day07.practice import mod_book


class Member(ABC):
    def __init__(self, m_member_id, m_name, m_password):
        self.member_id = m_member_id
        self.name = m_name
        self.__password: str = m_password
        self.__borrowed_books: list[mod_book.Book] = []

    def get_password(self):
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book: mod_book.Book):
        if len(self.__borrowed_books) < self.get_max_books():
            if book.decrease_stock():
                self.__borrowed_books.append(book)
        else:
            print("您当前已达到最大借阅数量!")

    def return_book(self, book: mod_book.Book):
        if book in self.__borrowed_books:
            # 还书 , 恢复库存

            # 把列表中的已借阅的书籍归还
            self.__borrowed_books.remove(book)
            print(f"{book.title} 归还成功!")
        else:
            print("当前书籍不存在,无法归还 . . .")

    @abstractmethod
    def get_max_books(self):
        pass


# 普通会员
class NormalMember(Member):
    def get_max_books(self):
        return 3


# VIP会员
class VIPMember(Member):
    def __init__(self, m_member_id, m_name, m_password, m_vip_level):
        Member.__init__(self, m_member_id, m_name, m_password)
        self.vip_level = m_vip_level

    def get_max_books(self):
        return 6 + self.vip_level
