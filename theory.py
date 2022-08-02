from icecream import ic
from emoji import list_to_emoji
from conversion import list2array, list2dict, arr_to_relative, relative_breakdown


def turns_needed(hand):
    # basic
    def search_turns_basic(_list):
        def m_d_adder(_m_d_list, m, d):
            _m_d_list[0] += m
            _m_d_list[1] += d

        def count_m_d(breakdown_list):
            m_d_counter = [0, 0]
            head = False
            for i in breakdown_list:
                if len(i) == 3:
                    m_d_adder(m_d_counter, 1, 0)
                if len(i) == 2:
                    m_d_adder(m_d_counter, 0, 1)
                    if not head and i[0] == i[1]:
                        head = True
            return calculate_steps(*m_d_counter, head)

        def calculate_steps(m, d, head):
            # Reference: https://www.bilibili.com/read/cv10974292
            c = max(m + d - 5, 0)
            q = 0 if m + d > 4 and not head else 1
            return 9 - 2 * m - d + c - q

        relative = arr_to_relative(list2array(hand))
        collection = relative_breakdown(relative)
        return min([count_m_d(b_list) for b_list in collection])



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

    return (search_turns_basic(hand),
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
