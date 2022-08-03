from emoji import list_to_emoji, id_to_emoji
from theory import turns_needed


# hand analysis
def hand_analysis(player):
    print(f'{player}: {list_to_emoji(player.hand)}, {turns_needed(player.hand)}')


def print_game_info(_p_list, _d):
    print('-' * 50)
    print(f'Dora Indicator: ', end='')
    print(list_to_emoji(_d))

    print(f'Rounds: {min([len(i.tile_river) + 1 for i in _p_list])}')

    for i in _p_list:
        print(f'{i} \nTile river: ', end='')
        print(list_to_emoji(i.tile_river))
    print('-' * 50)


def print_player_hand(_p, _d = None):
    print(f'{_p} hand: ', end='')
    print(f'{list_to_emoji(_p.hand)}  {id_to_emoji(_d)}')


def print_effective(_total_effectiveness_list):
    for index, effectiveness_dict in enumerate(_total_effectiveness_list):
        if index == 0:
            print('一般型')
        if index == 1:
            print('七对子')
        if index == 2:
            print('国士无双')
        for k, v in effectiveness_dict.items():
            print(f'discard: {id_to_emoji(k)} waiting: {list_to_emoji(v)}')
