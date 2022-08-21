from player import Player


class CPU(Player):
    def __init__(self, name='Default'):
        super(CPU, self).__init__(name)



if __name__ == '__main__':
    cpu = CPU()
    print(cpu.hand)