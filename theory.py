from icecream import ic
from collections import deque
from emoji import list_to_emoji
from tiles import tile_index
from conversion import list2array, list2count_list, list2dict


def turns_needed(hand):
    # basic
    arr = list2array(hand)

    def head_candidates(list):
        candidates = set()
        cache = -1
        for i in list:
            if i == cache: candidates.add(i)
            cache = i
        return candidates

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

    def arr_to_relative(arr):
        relative_arr = []
        for i, _a in enumerate(arr):
            if i < 3:
                relative_arr += [m_list2relation(_a, False)]
            else:
                relative_arr += [m_list2relation(_a, True)]

        return relative_arr

    def search_turns_basic(relative_list):

        def m_d_adder(_m_d_list, m, d):
            _m_d_list[0] += m
            _m_d_list[1] += d

        def m_d_counter(m_list, index):
            success = False
            m_d_list = [0, 0]
            for s_list in m_list:
                if len(s_list) < 2: continue
                if len(s_list) == 2:
                    m_d_adder(m_d_list, 0, 1)
                else:
                    ic(m_list)
                    ic(s_list)
                    count_dict = list2dict(s_list)
                    # exact triple
                    m_d_triple_list = [0, 0]
                    for i, (k, v) in enumerate(count_dict.items()):
                        if v > 2:
                            new_s_list = s_list.copy()
                            for _ in range(3):
                                new_s_list.remove(k)
                            m_d_adder(m_d_triple_list, 1, 0)
                            success = True
                            new_m_list = arr_to_relative(list2array(new_s_list))[index]
                            m_d_adder(m_d_triple_list, *(m_d_counter(new_m_list, index)))
                    # exact straight
                    m_d_straight_list = [0, 0]
                    if index < 3:  # character yes/no?
                        keys = count_dict.keys()
                        if len(keys) > 2:
                            c1, c2 = -10, -10
                            for i in keys:
                                if i - 2 == c1 - 1 == c2:
                                    new_s_list = s_list.copy()
                                    new_s_list.remove(i)
                                    new_s_list.remove(c1)
                                    new_s_list.remove(c2)
                                    m_d_adder(m_d_straight_list, 1, 0)
                                    success = True
                                    new_m_list = arr_to_relative(list2array(new_s_list))[index]
                                    m_d_adder(m_d_straight_list, *(m_d_counter(new_m_list, index)))
                                else:
                                    c2 = c1
                                    c1 = i

                    if m_d_triple_list[0] > m_d_straight_list[0]:
                        m_d_adder(m_d_list, *m_d_triple_list)
                    else: m_d_adder(m_d_list, *m_d_straight_list)

                    if not success:
                        new_s_list = s_list.copy()
                        m_d_adder(m_d_list, 0, 1)
                        ic(new_s_list)
                        new_m_list = arr_to_relative(list2array(new_s_list[2:]))[index]
                        ic(new_m_list)
                        m_d_adder(m_d_list, *(m_d_counter(new_m_list, index)))

            return m_d_list

        total_m_d_list = [0, 0]
        for index, m_list in enumerate(relative_list):
            m_d_adder(total_m_d_list, *m_d_counter(m_list, index))

        def calculate_steps(m, d):
            # Reference: https://www.bilibili.com/read/cv10974292
            m, d, c, q = [0] * 4
            c = max(m + d - 5, 0)
            q = 0 if m + d > 4 and len(head_candidates(hand)) == 0 else 1
            return 9 - 2 * m - d + c - q

        return calculate_steps(*total_m_d_list)



    # seven pairs
    def search_turns_seven_pairs(_list):
        """
        :param _list:hand list
        :return: the turns to format seven pairs type
        """
        turns = 6
        for _v in list2dict(_list).values():
            if _v > 1: turns -= 1
        return turns

    # thirteen 19 tiles
    def search_turns_thirteen_19_tiles(_list):
        """
        :param _list: hand list
        :return: the turns to format thirteen 19 tiles type
        """
        turns = 12
        one_nine = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
        for _k in list2dict(_list).keys():
            if _k in one_nine: turns -= 1
        return max(turns, 0)

    return (search_turns_basic(arr_to_relative(arr)),
            search_turns_seven_pairs(hand),
            search_turns_thirteen_19_tiles(hand))


list = [0, 2, 5, 8, 8, 11, 12, 23, 28, 29, 31, 32, 33]
# list = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
ic(list_to_emoji(list))
ic(turns_needed(list))
