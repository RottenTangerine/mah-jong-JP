from collections import defaultdict
import numpy as np


def count_dict(l: list):
    c_dict = defaultdict(int)
    for i in set(l):
        c_dict[i] = l.count(i)
    return c_dict


def check(list):
    def _chowability(list: list):
        __chowable_list = []
        return __chowable_list

    def _pungability(list: list):
        __pungable_list = []
        return __pungable_list

    def _kongability(list: list):
        __kongable_list = []
        return __kongable_list

    _c_dict = count_dict(list)
    _chowable_list = _chowability(_c_dict)
    _pungable_list = _pungability(_c_dict)
    _kongable_list = _kongability(_c_dict)


if __name__ == '__main__':
    list = [4, 7, 10, 13, 13, 13, 23, 25, 27, 31, 32, 33, 33]
    list = np.asarray(list)

    print(count_dict(list))
    for i in range(34):
        c_d = count_dict(list)
        print(f'{i}: {bool(c_d[i])}')
    list2 = [count_dict(list)[i] for i in range(34)]
    print(list2)
