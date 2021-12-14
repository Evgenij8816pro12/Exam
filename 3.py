class Tomato:
    states = {1: Green, 2: Dairy, 3: Blange, 4: Ripe}

    def __init__(self, _index, _state=states[1]):
        self._index = _index
        self._state = _state

    def grow(self, _state):
        self._state += 1

    def is_ripe(self):
        if self._state == states[4]:
            print("Tomato ripe")
        else:
            print("Tomato is not mature, look after more")


class TomatoBush(Tomato):
    def __init__(self, tomatoes):
        super().__init__()
        self.tomatoes = []

    def grow_all(self):
        i = 0
        for i in self.tomatoes:
            i += 1

    def all_are_ripe(self):
        for i in self.tomatoes:
            if i == states[4]:
                print("True")
            else:
                print("False")

    def give_away_all(self):
        self.tomatoes.pop(index(states[4]))


class Gardener(TomatoBush):

    def __init__(self, name, _plant):
        super().__init__()
        self.name = name
        self._plant = _plant

    def work(self, _state):
        _state += 1
        return _state

    def harvest(self):
        for i in self.tomatoes:
            if i == states[4]:
                print("The fruits are ripe, the gardener is harvesting")
            else:
                print("The fruits are not ripe")

    @staticmethod
    def knowledge_base():
        print("Gardening reference")


if __name__ == '__main__':

    test = Gardener()
    print(test.knowledge_base())
    pomm = TomatoBush()
    pamm = Gardener()
    print(pamm.work())
    print(pomm.all_are_ripe())
    print(pamm.work())
    print(pamm.harvest())

