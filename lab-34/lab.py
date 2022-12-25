a = [1, 2, 3]
b = [(1, 1), (2, 4), (3, 9)]
# #1
# a = b
# print(a)
#2
# a = [g for g in b]
# print(a)
#3
# a = b.copy()
# print(a)
#4
# a = b[:]
# print(a)
#5
# for i in b: a.append(i)
# a = a[3:6]
# print(a)
# 6
# a = [(i,i**2) for i in a]
# print(a)
#7
# a = list(zip(a,map(lambda x:(x**2), a)))
# print(a)