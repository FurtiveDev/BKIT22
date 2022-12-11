from operator import itemgetter


class Book:
    """Книга"""

    def __init__(self, id, price, name, shop_id):
        self.id = id
        self.price = price
        self.name = name
        self.shop_id = shop_id


class Shop:
    """Книжный магазин"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class BookShop:
    """ 'Книги магазина' для реализации связи многие-ко-многим """

    def __init__(self, shop_id, book_id):
        self.shop_id = shop_id
        self.book_id = book_id


Shops = [
    Shop(1, 'Книжный червь'),
    Shop(2, 'Книголюб'),
    Shop(3, 'Дом книг'),
    Shop(4, 'Мир книг'),
    Shop(5, 'Перечитай-город'),
]

Books = [
    Book(1, 68, 'Конституция Российской Федерации', 1),
    Book(2, 666, 'Божественная комедия', 2),
    Book(3, 1010, 'Совершенный алгоритм', 2),
    Book(4, 2200, 'Война и мир', 3),
    Book(5, 100, 'Сто лет одиночества', 3),
    Book(6, 1852, 'Муму', 4),
    Book(7, 1988, 'Остров сокровищ', 5)
]

Books_Shops = [
    BookShop(1, 1),
    BookShop(2, 2),
    BookShop(2, 3),
    BookShop(3, 4),
    BookShop(3, 5),
    BookShop(4, 6),
    BookShop(5, 7)
]

one_to_many = [(b.name, b.price, s.name)
               for s in Shops
               for b in Books
               if b.shop_id == s.id]

many_to_many_temp = [(s.name, bs.shop_id, bs.book_id)
                     for s in Shops
                     for bs in Books_Shops
                     if s.id == bs.shop_id]

many_to_many = [(b.id, shop_id)
                for name, shop_id, book_id in many_to_many_temp
                for b in Books if b.id == book_id]
