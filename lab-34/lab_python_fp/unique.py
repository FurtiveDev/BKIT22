class Unique(object):
    def __init__(self, items, **kwargs):
        self.result = []
        for key, value in kwargs.items():
            if not (key == 'ignore_case' and value == True):
                break
            for i in range(len(items)):
                try:
                    items[i] = items[i].lower()
                finally:
                    continue
        for i in items:
            if i not in self.result:
                self.result.append(i)

    def __next__(self):
        try:
            element = self.result[self.cur]
            self.cur += 1
            return element
        except:
            raise StopIteration

    def __iter__(self):
        self.cur = 0
        return self

a = Unique([1,5,7,2,4,6,4,3,6,3,4,2]).result
print(a)
b = ['A', 'a', 'B', 'b']
print(Unique(b).result)
for i in Unique(b, ignore_case=True):
    print(i, end = ' ')