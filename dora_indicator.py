from CircularLinkedList import CircularLinkedList
from tiles import tile_index, id2suit


class Indicator(CircularLinkedList):
    stack = tile_index
    for i, j in stack.items():
        exec(f"""{i} = CircularLinkedList()\nfor i in {j}:\n\t{i}.append(i)""")

    def __init__(self):
        super().__init__()

    def find_dora(self, type_id):
        return eval(f'self.{id2suit(type_id)}.search({type_id}).next.data')


if __name__ == '__main__':
    indicator = Indicator()
    test_id = 26
    output = indicator.find_dora(test_id)
    from emoji import id_to_emoji
    print(f"Dora Indicator:{id_to_emoji(test_id)}, Dora:{id_to_emoji(output)}")
