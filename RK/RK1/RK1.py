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


def main():
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

    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(list(res_11))

    print('Задание А2')
    res_12_unsorted = []
    for s in Shops:
        s_emps = list(filter(lambda i: i[2] == s.name, one_to_many))
        if len(s_emps) > 0:
            s_prices = [price for _, price, _ in s_emps]
            s_prices_sum = sum(s_prices)
            res_12_unsorted.append((s.name, s_prices_sum))
    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)
    print('Задание А3') # Если в названии магазина содержится слово "книг"
    res_13 = []
    for i in filter(lambda a: "книг" in Shops[a[1] - 1].name, many_to_many): #Убираем повторы
            a = ((Shops[i[1] - 1].name, [_.name for _ in filter(lambda a: a.shop_id == i[1], Books)]))
            if a not in res_13:
                res_13.append(a)
    print(res_13)


if __name__ == '__main__':
    main()
