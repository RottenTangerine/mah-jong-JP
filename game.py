import random
from collections import deque
from dora_indicator import Indicator
from tiles import tile_index
from emoji import id_to_emoji

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
for i in sorted(player_1):
    print(id_to_emoji(i), end='')

# draw
player_1.append(stack.popleft())
