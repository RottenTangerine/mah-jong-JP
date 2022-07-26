from icecream import ic
import random
from collections import deque
from dora_indicator import Indicator
from tiles import tile_index
from emoji import id_to_emoji, list_to_emoji
from player import Player
from hand import check

# game init
main_wind = 0  # east wind
player_wind = [0, 1, 2, 3]
player_1 = Player('player_1')
player_2 = Player('player_2')
player_3 = Player('player_3')
player_4 = Player('player_4')
player_order = [player_1, player_2, player_3, player_4]
random.shuffle(player_order)
for p, w in zip(player_order, player_wind):
    p.wind = w

# shuffle cards
stack = list(range(0, 34)) * 4
stack = deque(stack)
random.shuffle(stack)
print(f'stack: {list_to_emoji(stack)}')

# ace tile
ace = []
for i in range(14):
    ace.append(stack.pop())
ace = ace[::-1]
print(f"ace: {list_to_emoji(ace)}")

ridge_tile_list = [ace[-2], ace[-1], ace[-4], ace[-3]]
dora_list=ace[-6::-2]
hidden_dora_list=ace[-5::-2]
print(f'ridge tile: {list_to_emoji(ridge_tile_list)}')
print(f'dora: {list_to_emoji(dora_list)}')
print(f'hidden dora: {list_to_emoji(hidden_dora_list)}')

# dora
dora_indicator_list = []
dora_indicator = Indicator()

dora_indicator_list.append(ace[-5])

# deal tile
for i in range(3):
    for p in player_order:
        for i in range(4):
            p.hand.append(stack.popleft())

for p in player_order:
    p.hand.append(stack.popleft())
    p.hand.sort()


def print_game_info(_p, _d):
    print('-' * 50)
    print(f'Dora Indicator: ', end='')
    print(list_to_emoji(_d))

    print(f'Rounds: {min([len(i.tile_river) + 1 for i in _p])}')

    for i in _p:
        print(f'{i} \nTile river: ', end='')
        print(list_to_emoji(i.tile_river))
    print('-' * 50)


def print_hand_info(_p, _d):
    print('Your Turn:')
    print(f'{_p} hand: ', end='')
    print(list_to_emoji(_p.hand), end='')
    print(f'  {id_to_emoji(_d)}')


# draw
while True:
    if not stack: break
    player_index = player_order[0]
    for player in player_order:
        if player != player_index: continue

        if not stack:
            break
        print_game_info(player_order, dora_indicator_list)

        #  self-drawn
        drawn = stack.popleft()
        player.hand.append(drawn)
        # print_hand_info(player, drawn)

        # self hand check
        # print(check(player.hand, drawn))

        # discarding a tile
        discard = player.hand.pop(0)
        player.tile_river.append(discard)
        player.hand = sorted(player.hand)

        # others hand check
        # for i in player_order:
            # print(check(i.hand, discard))
        # skip player
        player_index = player_order[(player_order.index(player) + 1) % 4]
    else:
        continue
    break


# count multiples:

# calculate fu
def check_hand():
    fu, multiples = 0, 0
    pass
    return fu, multiples


# calculate pts
def cal_pt(fu, multiples):
    if multiples < 5:
        return min(fu * 2 ** (multiples + 2), 2000)
    else:
        if multiples == 5 : return 2000
        if 5 < multiples < 8: return 3000
        if 8 <= multiples< 11: return 4000
        if 11 <= multiples < 14: return 6000
    return 8000
