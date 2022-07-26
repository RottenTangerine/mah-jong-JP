tile_index = {'characters': range(0, 9),
              'dots': range(9, 18),
              'sticks': range(18, 27),
              'winds': range(27, 31),
              'dragons': range(31, 34), }
TILE_TYPES = 34


def id2suit(id):
    for i, j in tile_index.items():
        if id in j: return i
    return None


def id2suit_id(id):
    for x, (i, j) in enumerate(tile_index.items()):
        if id in j: return x
    return None


def id2wind(id):
    if id in tile_index['winds']:
        return tile_index['winds'][id - 27]
    if id + 27 in tile_index['winds']:
        return tile_index['winds'][id]


class Tile:
    def __init__(self):
        self.id = None
        self.owner = None
        self.isDora = False
        self.isRed = False
        self.isGreen = False
        self.isMiddle = False

    def __str__(self):
        return self.id

if __name__ == '__main__':
    print(id2wind(2))
