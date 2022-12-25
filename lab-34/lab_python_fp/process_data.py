import json
from field import field
from gen_random import gen_random
from print_result import print_result
from unique import Unique
import cm_timer


path = "data_light.json"

f = open(path, 'r', encoding='utf-8')
data = json.load(f)
a = data.copy


@print_result
def f1(data):
    return list(Unique(field(data, 'job-name'), ignore_case=True))


@print_result
def f2(data):
    return list(filter(lambda el: el.startswith('программист'), data))


@print_result
def f3(data):
    return list(map(lambda x: x + ' с опытом Python', data))


@print_result
def f4(data):
    return list(zip(data, gen_random(len(data), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer.cm_timer_1() as c:
        f4(f3(f2(f1(data))))
