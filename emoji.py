from tiles import id2suit

offset = {'characters': 126983,
          'dots': 127001-9,
          'sticks': 126992-18,
          'winds': 126976-27,
          'dragons': 126980-31}

def id_to_emoji(id):
    return chr(id + offset[id2suit(id)])


if __name__ == '__main__':
    print(id2suit(1))
    print(id_to_emoji(9))

