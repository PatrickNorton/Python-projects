from multiprocessing import Pool
import math

def test_func(i):
    j = 0
    for x in range(1000000):
        j += math.atan2(i, i)
    return j

if __name__ == '__main__':
    var = range(500)
    p = Pool()
    var = map(test_func, var)
