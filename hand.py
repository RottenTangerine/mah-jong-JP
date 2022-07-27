from icecream import ic
from tiles import TILE_TYPES as tts, tile_index, id2suit, id2suit_id
from collections import deque
from conversion import list2array
import numpy as np


def count_dict(l):
    return {i: np.sum(l == i) for i in range(tts)}


def check(hand, _tile):

    # only occurs in same suit
    arr = list2array(hand)
    arr = arr[id2suit_id(_tile)]
    hand.append(_tile)

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

    def _rongability(hand: list, __tile):
        def rong_checker(l):
            if len(l) != 0 and len(l) < 2: return False
            if not l: return True
            l = deque(l)
            first = l.popleft()
            second = l.popleft()
            if not l:
                return True if first == second else False  # last double
            third = l.popleft()
            if first == second - 1 == third - 2:
                return rong_checker(l)

            if first == second == third:
                if rong_checker(l): return True

            if first == second:
                l.appendleft(third)
                if rong_checker(l): return True

            return False

        arr = list2array(sorted(hand))
        return np.all([rong_checker(i) for i in arr])

    return [_chiiability(arr, _tile), _pongability(arr, _tile), _kongability(arr, _tile), _rongability(hand, _tile)]


if __name__ == '__main__':
    from tiles import id2suit_id
    from emoji import id_to_emoji

    # hand = [3, 3, 3, 4, 4, 4, 5, 5, 5, 14, 14, 14, 22]
    hand = [0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 8]
    for i in hand:
        print(id_to_emoji(i), end='')

    tile = 5
    print(' ', end='')
    print(id_to_emoji(tile))

    # test
    print(check(hand, tile))
