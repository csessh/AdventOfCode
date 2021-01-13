#!/Users/thangdo/Documents/dev/csessh/bin/python


class Location:
    map_width = 0
    map_depth = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_destination = False

    def go_east(self, steps: int):
        self.x += steps

        if self.x >= Location.map_width:
            self.x -= Location.map_width

    def go_south(self, steps: int):
        self.y += steps

        if self.y >= Location.map_depth:
            self.is_destination = True


class Traveller:
    def __init__(self):
        with open('test.txt', 'r') as f:
            self._map = [line.strip() for line in f.readlines()]
            Location.map_depth = len(self._map)
            Location.map_width = len(self._map[0])
        self._location = Location(0, 0)
        self.trees_encountered = 0

    def travel(self, east: int, south: int):
        while not self._location.is_destination:
            self._location.go_east(east)
            self._location.go_south(south)

            try:
                if self._map[self._location.y][self._location.x] == '#':
                    self.trees_encountered += 1
            except IndexError:
                # We don't count this last step as we're already out of bounds
                pass

    def reset(self):
        self._location = Location(0, 0)
        self.trees_encountered = 0


def solve_part1():
    me = Traveller()
    me.travel(3, 1)
    print(me.trees_encountered)
    me.reset()


def solve_part2():
    me = Traveller()
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    probability_of_sudden_arboreal_stop = 1
    for slope in slopes:
        me.travel(slope[0], slope[1])
        print(me.trees_encountered)
        probability_of_sudden_arboreal_stop *= me.trees_encountered
        me.reset()

    print(probability_of_sudden_arboreal_stop)


solve_part1()
solve_part2()
