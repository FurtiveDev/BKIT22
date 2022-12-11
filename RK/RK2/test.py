from unittest import TestCase, main
from RK1 import *


class order_test(TestCase):
    def test_1(self):
        expected_result_for_A1 = [('Война и мир', 2200, 'Дом книг'),
                                  ('Сто лет одиночества', 100, 'Дом книг'),
                                  ('Божественная комедия', 666, 'Книголюб'),
                                  ('Совершенный алгоритм', 1010, 'Книголюб'),
                                  ('Конституция Российской Федерации', 68, 'Книжный червь'),
                                  ('Муму', 1852, 'Мир книг'),
                                  ('Остров сокровищ', 1988, 'Перечитай-город')]
        res_A1 = list(sorted(one_to_many, key=itemgetter(2)))
        self.assertEqual(res_A1, expected_result_for_A1)

    def test_2(self):
        expected_result_for_A2 = [('Книжный червь', 68), ('Книголюб', 1676),
                                  ('Мир книг', 1852), ('Перечитай-город', 1988),
                                  ('Дом книг', 2300)]
        res_A2_unsorted = []
        for s in Shops:
            s_emps = list(filter(lambda i: i[2] == s.name, one_to_many))
            if len(s_emps) > 0:
                s_prices = [price for _, price, _ in s_emps]
                s_prices_sum = sum(s_prices)
                res_A2_unsorted.append((s.name, s_prices_sum))
        res_A2 = sorted(res_A2_unsorted, key=itemgetter(1))
        self.assertEqual(res_A2, expected_result_for_A2)

    def test_3(self):
        expected_result_for_A3 = [('Дом книг', ['Война и мир', 'Сто лет одиночества']),
                                  ('Мир книг', ['Муму'])]
        res_A3 = []
        for i in filter(lambda a: "книг" in Shops[a[1] - 1].name, many_to_many):
            a = ((Shops[i[1] - 1].name, [_.name for _ in filter(lambda a: a.shop_id == i[1], Books)]))
            if a not in res_A3:
                res_A3.append(a)
        self.assertEqual(res_A3, expected_result_for_A3)


if __name__ == '__main__':
    main()
