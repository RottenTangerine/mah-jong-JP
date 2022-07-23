import random
from collections import deque
from dora_indicator import Indicator
from tiles import tile_index
from emoji import id_to_emoji

# game init
main_wind = 0  # east wind
player_1_wind = 0  # east
player_2_wind = 1  # south
player_3_wind = 2  # west
player_4_wind = 3  # north

player_1_tile_river = []
player_2_tile_river = []
player_3_tile_river = []
player_4_tile_river = []

# shuffle cards
stack = list(range(0, 34)) * 4
stack = deque(stack)
random.shuffle(stack)
print(stack)

ace = []
for i in range(14):
    ace.append(stack.pop())
ace = ace[::-1]
print(f"ace: {[id_to_emoji(i) for i in ace]}")

dora_indicator = Indicator()

# deal
player_1 = []
player_2 = []
player_3 = []
player_4 = []
for i in range(3):
    for i in range(4): player_1.append(stack.popleft())
    for i in range(4): player_2.append(stack.popleft())
    for i in range(4): player_3.append(stack.popleft())
    for i in range(4): player_4.append(stack.popleft())

player_1.append(stack.popleft())
player_2.append(stack.popleft())
player_3.append(stack.popleft())
player_4.append(stack.popleft())

player_1.sort()
print(player_1)
for i in sorted(player_1):
    print(id_to_emoji(i), end='')

# draw
order = [player_1, player_2, player_3, player_4]
while True:
    if not stack:
        break
    for player in order:
        if not stack:
            break
        player.append(stack.popleft())
        #  self-drawn
        # discarding a tile
        # chow pung kong
        # skip player
    else:
        continue
    break


# count pts

# calculate fu
def check_hand():
    fu, multiple = 0, 0
    pass
    return fu, multiple


# calculate pts
def cal_pt(fu, multiple):
    basic_pt = fu * 2 ** (multiple + 2)
