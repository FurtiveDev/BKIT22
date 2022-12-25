import math


def get_roots(a, b, c):
    result = []
    D = b * b - 4 * a * c
    if D == 0.0:
        t = -b / (2.0 * a)
        result.append(math.sqrt(t))
        result.append(-math.sqrt(t))
    elif D > 0.0:
        sqD = math.sqrt(D)
        t1 = ((-b + sqD) / (2.0 * a))
        t2 = ((-b - sqD) / (2.0 * a))
        if (t1 > 0):
            result.append(-math.sqrt(t1))
            result.append(math.sqrt(t1))
        if (t2 > 0):
            result.append(-math.sqrt(t2))
            result.append(math.sqrt(t2))
        elif (t1 == 0 or t2 == 0):
            result.append(0.0)
    return set(result)