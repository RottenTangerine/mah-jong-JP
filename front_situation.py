from icecream import ic
from tiles import TILE_TYPES as TTS
import pickle


def tile_remains_dict(player, player_o, dora_indicator):
    tile_remains = {i: 4 for i in range(TTS)}
    for i in dora_indicator:
        update_tile_remains_dict(tile_remains, i)
    for _player in player_o:
        for _tile in _player.tile_river:
            update_tile_remains_dict(tile_remains, _tile)
    for _tile in player.hand:
        update_tile_remains_dict(tile_remains, _tile)
    return tile_remains


def update_tile_remains_dict(tile_remains, tile):
    tile_remains[tile] -= 1


if __name__ == '__main__':
    from emoji import list_to_emoji
    with open('test.txt', 'rb') as f:
        player_order = pickle.load(f)
    print(player_order)
    for _p in player_order:
        print(f"{_p} tile river: {list_to_emoji(_p.tile_river)}")

    ic(tile_remains_dict(player_order[0], player_order, [13]))
