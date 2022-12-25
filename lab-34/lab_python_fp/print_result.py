def print_result(func):
    def wrapper(data):
        print(func.__name__)
        result = func(data)
        if (type(result) == list):
            for i in result:
                print(i)
        elif (type(result) == dict):
            for key, value in result.items():
                print(key, '=', value, sep='')
        else:
            print(result)
        return result

    return wrapper


@print_result
def test_1(a):
    return a


@print_result
def test_2(a):
    return a


@print_result
def test_3(a):
    return {'a': 1, 'b': 2}


@print_result
def test_4(a):
    return a


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1(1)
    test_2('ui5')
    test_3({'a': 1, 'b': 2})
    test_4([1, 2])