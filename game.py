from icecream import ic
import random
from collections import deque
from dora_indicator import Indicator
from tiles import tile_index
from emoji import id_to_emoji
from player import Player

# game init
main_wind = 0  # east wind
player_wind = [0, 1, 2, 3]
random.shuffle(player_wind)
player_1 = Player()
player_2 = Player()
player_3 = Player()
player_4 = Player()
player_list = [player_1, player_2, player_3, player_4]
for p, w in zip(player_list, player_wind):
    p.wind = w

ic(player_1.wind)

# shuffle cards
stack = list(range(0, 34)) * 4
stack = deque(stack)
random.shuffle(stack)

# ace tile
ace = []
for i in range(14):
    ace.append(stack.pop())
ace = ace[::-1]
print(f"ace: {[id_to_emoji(i) for i in ace]}")


# dora
dora_indicator = Indicator()

# deal tile
for i in range(3):
    for p in player_list:
        for i in range(4):
            p.hand.append(stack.popleft())

for p in player_list:
    p.hand.append(stack.popleft())

player_1.hand.sort()
for i in sorted(player_1.hand):
    print(id_to_emoji(i), end='')

# draw
# order = [player_1, player_2, player_3, player_4]
# while True:
#     if not stack:
#         break
#     for player in order:
#         if not stack:
#             break
#         #  self-drawn
#         player.append(stack.popleft())
#         # discarding a tile
#
#         # chow pung kong
#         # skip player
#     else:
#         continue
#     break


# count pts

# calculate fu
def check_hand():
    fu, multiple = 0, 0
    pass
    return fu, multiple


# calculate pts
def cal_pt(fu, multiple):
    basic_pt = fu * 2 ** (multiple + 2)
