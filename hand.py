from icecream import ic
from tiles import TILE_TYPES as tts, tile_index, id2suit, id2suit_id
from collections import deque
import numpy as np


def hand2array(l:list):
    _tile_list = deque(l)
    array = []
    for i, j in tile_index.items():
        short_arr = []
        while _tile_list:
            _tile = _tile_list.popleft()
            if _tile in j:
                short_arr = short_arr + [_tile]
                continue
            break
        _tile_list.appendleft(_tile)
        array += [short_arr]
    return array


def count_dict(l):
    return {i: np.sum(l == i) for i in range(tts)}


def check(arr, _tile):
    # only occurs in same suit
    arr = arr[id2suit_id(_tile)]
    def _chiiability(arr, __tile):
        # chowable range
        set1 = set(tile_index[id2suit(_tile)])
        set2 = range(_tile - 2, _tile + 3)
        new_set = set.intersection(set1, set2)

        def _next(i):
            if __tile + i in new_set and (__tile + i) in arr:
                return True
            return False
        a = (__tile - 2, __tile - 1) if _next(-1) and _next(-2) else False
        b = (__tile - 1, __tile + 1) if _next(-1) and _next(1) else False
        c = (__tile + 1, __tile + 2) if _next(1) and _next(2) else False
        return [a, b, c]

    def _pongability(arr, __tile):
        return True if arr.count(_tile) > 1 else False

    def _kongability(arr, __tile):
        return True if arr.count(__tile) > 2 else False

    def _rongability(arr, __tile):
        pass

    return [_chiiability(arr, _tile), _pongability(arr, _tile), _kongability(arr, _tile)]


if __name__ == '__main__':
    from tiles import id2suit_id
    hand = [4, 6, 10, 13, 13, 13, 23, 24, 25, 31, 31, 32, 33]

    arr = hand2array(hand)
    ic(arr)
    ic(check(arr, 13), check(arr, 31))
    ic(10 in arr[id2suit_id(12)])



