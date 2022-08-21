from emoji import id_to_emoji
from tiles import id2wind

class Player(object):
    wind_list = ['east', 'south', 'west', 'north']

    def __init__(self, name='Default'):
        self.name = name
        self.point = 25000
        self.tile_river = []
        self.hand = []
        self.fulu = []
        self.lichi = False
        self.wind = -1

    def __str__(self):
        return f"{self.name}({self.point})  Wind:{self.wind_list[self.wind]}"
