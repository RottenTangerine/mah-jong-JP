from CircularLinkedList import CircularLinkedList
from tiles import tile_index


class Indicator(CircularLinkedList):
    stack = tile_index
    for i, j in stack.items():
        exec(f"""{i} = CircularLinkedList()\nfor i in {j}:\n\t{i}.append(i)""")

    def __init__(self):
        super().__init__()

    def id2suit(self, id):
        for i, j in tile_index.items():
            if id in j: return i
        return None

    def find_dora(self, type_id):
        return eval(f'self.{self.id2suit(type_id)}.search({type_id}).next.data')


if __name__ == '__main__':
    indicator = Indicator()
    output = indicator.find_dora(33)
    print(output)