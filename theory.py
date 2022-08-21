from icecream import ic
from emoji import list_to_emoji
from conversion import list2array, list2dict, arr_to_relative, relative_breakdown
from tiles import TILE_TYPES as TTS


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


def effective_draws(hand: list, draw):
    def discard_tile(_hand, _draw, _tile):
        _hand_copy = _hand.copy()
        _hand_copy.append(_draw)
        _hand_copy.remove(_tile)
        _hand_copy.sort()
        return _hand_copy

    def check_discard_and_forward(_hand, _draw):
        total_discard = []
        total_forward = []
        for index in range(3):
            discard_forward = []
            discard_stay = []
            forward = False
            # check if this draw useful
            current_turns_need = turns_needed(_hand)[index]
            for i in _hand:
                _hand_copy = discard_tile(_hand, _draw, i)
                new_turns_need = turns_needed(_hand_copy)[index]
                if new_turns_need < current_turns_need and i not in discard_forward:
                    forward = True
                    discard_forward.append(i)
                if new_turns_need == current_turns_need and i not in discard_stay:
                    discard_stay.append(i)
            if not forward:
                discard_stay.append(_draw)
            total_discard.append(discard_forward if forward else discard_stay)
            total_forward.append(forward)
        return total_discard, total_forward

    total_effectiveness_list = []
    discard_list = check_discard_and_forward(hand, draw)[0]
    for index in range(3):
        effectiveness_dict = {}
        for discard in discard_list[index]:
            hand_copy = discard_tile(hand, draw, discard)
            waiting_list = []
            for i in range(TTS):
                if check_discard_and_forward(hand_copy, i)[1][index]:
                    waiting_list.append(i)
            if waiting_list:
                effectiveness_dict[discard] = waiting_list
        total_effectiveness_list.append(effectiveness_dict)

    return total_effectiveness_list


if __name__ == '__main__':
    # list = [0, 2, 5, 8, 8, 11, 12, 23, 28, 29, 31, 32, 33]
    # list = [0, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33]
    # list = [3, 3, 3, 4, 4, 4, 5, 5, 5, 14, 14, 14, 22]
    # list = [0, 1, 4, 5, 10, 11, 12, 12, 12, 13, 14, 20, 21]
    l = [2, 4, 5, 6, 7, 7, 11, 12, 12, 24, 31, 33, 33]
    from printer import print_effective, id_to_emoji
    ic(arr_to_relative(list2array(l)))
    print(f'{list_to_emoji(l)}  {id_to_emoji(19)}')

    print_effective(effective_draws(l, 19))
