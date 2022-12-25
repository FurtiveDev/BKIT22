import time
from contextlib import contextmanager

class cm_timer_1():
    def __enter__(self):
        self.begin = time.time()
    def __exit__(self, type, value, traceback):
        print(time.time() - self.begin)

@contextmanager
def cm_timer_2():
    begin = time.time()
    yield
    print(time.time() - begin)

with cm_timer_1() as c:
    time.sleep(5.5)

# with cm_timer_2() as c:
#     time.sleep(5.5)