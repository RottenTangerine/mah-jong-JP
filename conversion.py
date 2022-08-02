from collections import deque
from tiles import tile_index
from itertools import product


def list2array(_list: list):
    """
    split hand tile list by suit
    :param _list: hand tile list
    :return: 2d list
    """
    _tile_list = deque(_list)
    array = []
    for i, j in tile_index.items():
        _tile = -1
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


def list2dict(_list: list):
    """
    count each element in list and convert result to dict
    :param _list: list
    :return: count dict
    """
    count_dict = {}
    for i in _list:
        if i in count_dict.keys():
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


def list2count_list(_list: list, length=9):
    """
    count each element in list and convert to count list
    :param _list: list
    :param length: length of the list, number tile is 9 (default)
    :return: count_list
    """
    count_list = [0] * length
    for i in _list:
        count_list[i] += 1
    return count_list


def m_list_to_relative_m_list(_m, is_number=True):
    """
    convert m_list to relative m_list
    :param _m: m_list
    :param is_number: is the tile is a number tile (character, circle, stick)
    :return:
    """
    m_list, s_list = [], []
    for _tile in _m:
        if not s_list:
            s_list.append(_tile)
            continue
        if not is_number:
            if _tile == s_list[-1]:
                s_list.append(_tile)
                continue
        else:
            if _tile - s_list[-1] < 3:
                s_list.append(_tile)
                continue
        m_list += [s_list]
        s_list = [_tile]
    else:
        m_list += [s_list]
    return m_list


def arr_to_relative(arr):
    """
    group close tiles together
    :param arr: array
    :return: relative array
    """
    relative_arr = []
    for i, _a in enumerate(arr):
        if i < 3:
            relative_arr += [m_list_to_relative_m_list(_a, True)]
        else:
            relative_arr += [m_list_to_relative_m_list(_a, False)]

    return relative_arr


def s_list_breakdown(s_list, index):
    """
    break down the s_list
    :param s_list: s_list
    :param index: index of s_list to m_list (to identify if the s_list is a number tile list)
    :return:
    """
    ans = []
    success = False
    if len(s_list) < 3:
        return [[s_list]]
    # exact triple
    new_m_list: list = s_list.copy()
    for k, v in list2dict(s_list).items():
        if v > 2:
            for _ in range(3):
                new_m_list.remove(k)
            new_relative_m_list = m_list_to_relative_m_list(new_m_list)
            if len(new_relative_m_list) == 2:
                left_s_list, right_s_list = new_relative_m_list
                for _s in product(s_list_breakdown(left_s_list, index), s_list_breakdown(right_s_list, index)):
                    _s = [i for i in _s]
                    ans.append([[k, k, k]] + _s)
            elif len(new_relative_m_list[0]) == 0:
                ans.append([[k, k, k]])
            else:
                for new_s_list in m_list_to_relative_m_list(new_m_list):
                    sub_ans = s_list_breakdown(new_s_list, index)
                    for _s in sub_ans:
                        ans.append([[k, k, k]] + _s)
            success = True
            break

    # exact straight
    if index < 3:
        keys = list2dict(s_list).keys()
        if len(keys) > 2:
            c1, c2 = -10, -10
            for i in keys:
                new_m_list: list = s_list.copy()
                if i - 2 == c1 - 1 == c2:
                    new_m_list.remove(i)
                    new_m_list.remove(c1)
                    new_m_list.remove(c2)
                    new_relative_m_list = m_list_to_relative_m_list(new_m_list)
                    if len(new_relative_m_list) == 2:
                        left_s_list, right_s_list = new_relative_m_list
                        sub_ans_combinations = product(s_list_breakdown(left_s_list, index),
                                                       s_list_breakdown(right_s_list, index))
                        for _s in sub_ans_combinations:
                            _s = _s[0] + _s[1]
                            ans.append([[c2, c1, i]] + _s)
                    elif len(new_relative_m_list[0]) == 0:
                        ans.append([[c2, c1, i]])
                    else:
                        for new_s_list in new_relative_m_list:
                            sub_ans = s_list_breakdown(new_s_list, index)
                            for _s in sub_ans:
                                ans.append([[c2, c1, i]] + _s)

                    success = True
                c2 = c1
                c1 = i
    # other
    if not success:
        i = 0
        for i in range(2, len(s_list), 2):
            ans.append(s_list[i - 2: i])
        else:
            ans.append(s_list[i:])
            ans = [ans]

    # drop duplicate
    for a in ans:
        for b in a:
            b.sort()
        a.sort()

    clean_ans = []
    for i in ans:
        if i not in clean_ans:
            clean_ans.append(i)
    return clean_ans


def relative_breakdown(relative_arr):
    def _unpacking(collection):
        arr = []
        for a in collection:
            s_arr = []
            for b in a:
                for c in b:
                    s_arr.append(c)
            arr.append(s_arr)
        return arr

    m_list_collection, s_list_collection = [[]] * 2
    for index, relative_m_list in enumerate(relative_arr):
        s_list_collection = [s_list_breakdown(s_list, index) for s_list in relative_m_list if s_list]
        s_list_collection = _unpacking([list(i) for i in product(*s_list_collection) if i])
        if s_list_collection:
            m_list_collection.append(s_list_collection)
    m_list_collection = _unpacking([list(i) for i in product(*m_list_collection) if i])
    return m_list_collection
