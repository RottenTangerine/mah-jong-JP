from tiles import tile_index

offset = {'characters': 126983,
          'dots': 127001-9,
          'sticks': 126992-18,
          'winds': 126976-27,
          'dragons': 126980-31}


def id2suit(id):
    for i, j in tile_index.items():
        if id in j: return i
    return None


def id_to_emoji(id):
    return chr(id + offset[id2suit(id)])


if __name__ == '__main__':
    print(id2suit(1))
    print(id_to_emoji(9))

