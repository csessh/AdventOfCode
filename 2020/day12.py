#!/Users/thangdo/Documents/dev/csessh/bin/python

from enum import Enum


class Heading(Enum):
    North = 0
    East = 1
    South = 2
    West = 3


class Coordinate:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def X(self) -> int:
        return self._x

    @X.setter
    def X(self, x):
        self._x = x

    @property
    def Y(self) -> int:
        return self._y

    @Y.setter
    def Y(self, y):
        self._y = y

    def calculate_manhattan_distant(self) -> int:
        return abs(self.X) + abs(self.Y)


class Ship:
    def __init__(self):
        self._location = Coordinate(0,0)
        self._heading = Heading.East

    def steer(self, side: str, value: int):
        if side == 'L':
            self._heading = Heading((self._heading.value - (value // 90)) % 4)
        elif side == 'R':
            self._heading = Heading((self._heading.value + (value // 90))% 4)

    def forward(self, units: int):
        if self._heading == Heading.North:
            self._location.Y += units

        if self._heading == Heading.East:
            self._location.X += units

        if self._heading == Heading.South:
            self._location.Y -= units

        if self._heading == Heading.West:
            self._location.X -= units

    def move(self, command: str):
        action = instruction[0]
        value = int(instruction[1:])

        if action == 'F':
            self.forward(value)
        elif action in 'NESW':
            original_heading = self._heading
            if action == 'N':
                self._heading = Heading.North

            if action == 'E':
                self._heading = Heading.East

            if action == 'S':
                self._heading = Heading.South

            if action == 'W':
                self._heading = Heading.West

            self.forward(value)
            self._heading = original_heading
        elif action in 'LR':
            self.steer(action, value)

        print(command, self._heading, self.location.X, self.location.Y)

    @property
    def location(self) -> Coordinate:
        return self._location


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        instructions = [row.strip() for row in f.readlines()]

    titanic = Ship()
    for instruction in instructions:
        titanic.move(instruction)
