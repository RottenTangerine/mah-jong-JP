from icecream import ic
from emoji import list_to_emoji
from conversion import list2array, list2dict, arr_to_relative


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
                    count_dict = list2dict(s_list)
                    # exact triple
                    m_d_triple_list = [0, 0]
                    m_d_triple_list_collection = []
                    for i, (k, v) in enumerate(count_dict.items()):
                        if v > 2:
                            small_m_d_triple_list = [0, 0]
                            new_s_list = s_list.copy()
                            for _ in range(3):
                                new_s_list.remove(k)
                            m_d_adder(small_m_d_triple_list, 1, 0)
                            success = True
                            new_m_list = arr_to_relative(list2array(new_s_list))[index]
                            m_d_adder(small_m_d_triple_list, *(m_d_counter(new_m_list, index)))
                            m_d_triple_list_collection += [small_m_d_triple_list]
                    if len(m_d_triple_list_collection) == 1:
                        m_d_adder(m_d_triple_list, *m_d_triple_list_collection[0])
                    elif len(m_d_triple_list_collection) > 1:
                        m_d_adder(m_d_triple_list, *max(m_d_triple_list_collection, key=lambda a: a[0]))

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
                    else:
                        m_d_adder(m_d_list, *m_d_straight_list)

                    if not success:
                        new_s_list = s_list.copy()
                        m_d_adder(m_d_list, 0, 1)
                        new_m_list = arr_to_relative(list2array(new_s_list[2:]))[index]
                        m_d_adder(m_d_list, *(m_d_counter(new_m_list, index)))
            return m_d_list

        def calculate_steps(m, d):
            # Reference: https://www.bilibili.com/read/cv10974292
            c = max(m + d - 5, 0)
            q = 0 if m + d > 4 and len(head_candidates(hand)) == 0 else 1
            return 9 - 2 * m - d + c - q

        total_m_d_list = [0, 0]
        for index, m_list in enumerate(relative_list):
            m_d_adder(total_m_d_list, *m_d_counter(m_list, index))
        ic(total_m_d_list)
        return calculate_steps(*total_m_d_list)

    # seven pairs
    def search_turns_seven_pairs(_list):
        """
        :param _list:hand list
        :return: the turns to format seven pairs type
        """
        turns = 6
        triple_counter = 0
        ic(list2dict(_list).values())
        for _v in list2dict(_list).values():
            if _v > 1: turns -= 1
            if _v > 2: triple_counter += 1
        return max(turns, triple_counter)

    # thirteen 19 tiles
    def search_turns_thirteen_19_tiles(_list):
        """
        :param _list: hand list
        :return: the turns to format thirteen 19 tiles type
        """
        turns = 13
        has_head = False
        one_nine = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
        for _k, _v in list2dict(_list).items():
            if _k in one_nine:
                turns -= 1
                if _v > 1: has_head = True
        if has_head:
            turns -= 1
        return max(turns, 0)

    return (search_turns_basic(arr_to_relative(arr)),
            search_turns_seven_pairs(hand),
            search_turns_thirteen_19_tiles(hand))


def effectie_draws(hand):
    for i in range(34):
        pass


if __name__ == '__main__':
    # list = [0, 2, 5, 8, 8, 11, 12, 23, 28, 29, 31, 32, 33]
    list = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
    # list = [3, 3, 3, 4, 4, 4, 5, 5, 5, 14, 14, 14, 22]
    list = [0, 1, 4, 5, 10, 11, 12, 12, 12, 13, 14, 20, 21]
    ic(arr_to_relative(list2array(list)))
    ic(list_to_emoji(list))
    ic(turns_needed(list))
