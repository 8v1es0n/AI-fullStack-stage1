class Book:
    def __init__(self, b_book_id, b_title, b_author, b_total_num):
        self.book_id = b_book_id
        self.title = b_title
        self.author = b_author
        self.total_num = b_total_num
        self.__available_num = b_total_num

    def __repr__(self):
        return (f"编号: {self.book_id} , 标题: {self.title} , "
                f"作者: {self.author} , 数量: {self.total_num} , 可借: {self.__available_num} ")

    def decrease_stock(self):
        if self.total_num > 0:
            self.__available_num -= 1
            return True
        else:
            print("库存不足, 借书失败 . . .")
            return False

    def increase_stock(self):
        self.__available_num += 1