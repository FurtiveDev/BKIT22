goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'},
]


def field(items, *args):
    result = []
    if (len(items) == 0):
        print("List of dicts is empty")

    assert len(args) > 0
    if len(args) == 1:
        result = [items[g][str(*args)] for g in range(len(items)) if str(*args) in items[g]]
        return result
    else:
        result = [{} for i in range(len(items))]
        for i in range(len(items)):
            for key in items[i]:
                if key in args:
                    result[i].update({key: items[i][key]})
    return result

print(field(goods, 'title'))
print(field(goods, 'title', 'price'))
