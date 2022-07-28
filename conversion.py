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


def arr_to_relative(arr):
    """
    group close tiles together
    :param arr:
    :return:
    """
    def m_list2relation(_a, character=False):
        m_list, s_list = [], []
        for _tile in _a:
            if not s_list:
                s_list.append(_tile)
                continue
            if character:
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

    relative_arr = []
    for i, _a in enumerate(arr):
        if i < 3:
            relative_arr += [m_list2relation(_a, False)]
        else:
            relative_arr += [m_list2relation(_a, True)]

    return relative_arr
