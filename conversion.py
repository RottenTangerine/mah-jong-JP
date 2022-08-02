from collections import deque
from tiles import tile_index


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
    :param arr:
    :return:
    """
    relative_arr = []
    for i, _a in enumerate(arr):
        if i < 3:
            relative_arr += [m_list_to_relative_m_list(_a, True)]
        else:
            relative_arr += [m_list_to_relative_m_list(_a, False)]

    return relative_arr


def s_list_breakdown(s_list, index):
    ans = []
    success = False
    if len(s_list) < 3:
        return [s_list]
    # exact triple
    new_m_list: list = s_list.copy()
    for k, v in list2dict(s_list).items():
        if v > 2:
            for _ in range(3):
                new_m_list.remove(k)
            success = True
            for new_s_list in m_list_to_relative_m_list(new_m_list):
                ans.append([[k, k, k]] + [s_list_breakdown(new_s_list, index)])

    # exact straight
    new_m_list: list = s_list.copy()
    if index < 3:
        keys = list2dict(s_list).keys()
        if len(keys) > 2:
            c1, c2 = -10, -10
            for i in keys:
                if i - 2 == c1 - 1 == c2:
                    new_m_list.remove(i)
                    new_m_list.remove(c1)
                    new_m_list.remove(c2)
                    success = True
                    for new_s_list in m_list_to_relative_m_list(new_m_list):
                        ans.append([[c2, c1, i]] + [s_list_breakdown(new_s_list, index)])
                else:
                    c2 = c1
                    c1 = i
    # other
    if not success:
        ans += [s_list[:2]] + s_list_breakdown(s_list[2:], index)

    return ans
