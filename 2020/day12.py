import math
from abc import abstractmethod
from enum import Enum


class Heading(Enum):
    North = 0
    East = 1
    South = 2
    West = 3


class Coordinate:
    def __init__(self, x: int, y: int):
        self.X = x
        self.Y = y

    @property
    def manhattan_distance_from_origin(self) -> int:
        return abs(self.X) + abs(self.Y)

    def __str__(self):
        x = 'East' if self.X > 0 else 'West'
        y = 'North' if self.Y > 0 else 'South'
        return f'({self.X}, {self.Y})'
        # return f'{self.X} units {x}, {self.Y} units {y}'


class Ship:
    def __init__(self):
        self._location = Coordinate(0, 0)

    @abstractmethod
    def steer(self, side: str, value: int):
        """
        How the ship steer given commands such as L90, L270 or R180 and so on...
        """
        pass

    @abstractmethod
    def forward(self, units: int):
        """
        Advance the ship in a given direction
        """
        pass

    @abstractmethod
    def shift(self, direction: str, value: int):
        """
        Shift the ship in a given diection without adjusting its heading
        """
        pass

    def action(self, command: str):
        """
        Translate command into meaningful action
        """
        action = command[0]
        value = int(command[1:])

        if action == 'F':
            self.forward(value)
        elif action in 'NESW':
            self.shift(action, value)
        elif action in 'LR':
            self.steer(action, value)

    @property
    def location(self) -> Coordinate:
        return self._location


# Part 1
class Titanic(Ship):
    def __init__(self):
        super().__init__()
        self._heading = Heading.East

    def steer(self, side: str, value: int):
        if side == 'L':
            self._heading = Heading((self._heading.value - (value // 90)) % 4)
        elif side == 'R':
            self._heading = Heading((self._heading.value + (value // 90)) % 4)

    def forward(self, units: int):
        if self._heading == Heading.North:
            self._location.Y += units

        if self._heading == Heading.East:
            self._location.X += units

        if self._heading == Heading.South:
            self._location.Y -= units

        if self._heading == Heading.West:
            self._location.X -= units

    def shift(self, direction: str, value: int):
        original_heading = self._heading
        if direction == 'N':
            self._heading = Heading.North
        elif direction == 'E':
            self._heading = Heading.East
        elif direction == 'S':
            self._heading = Heading.South
        elif direction == 'W':
            self._heading = Heading.West

        self.forward(value)
        self._heading = original_heading


# Part 2
class Ghost(Ship):
    def __init__(self, waypoint: Coordinate):
        super().__init__()
        self._waypoint = waypoint

    def steer(self, side: str, angle: int):
        angle = angle if side == 'L' else -angle
        radians = math.radians(angle)

        x = self._waypoint.X - self.location.X
        y = self._waypoint.Y - self.location.Y

        # Rotation matrix multiplication to get rotated x & y
        xr = int(x * math.cos(radians)) - int(y * math.sin(radians)) + self.location.X
        yr = int(x * math.sin(radians)) + int(y * math.cos(radians)) + self.location.Y
        self._waypoint = Coordinate(xr, yr)

    def forward(self, steps: int):
        x_units = (self._waypoint.X - self._location.X) * steps
        y_units = (self._waypoint.Y - self._location.Y) * steps

        self._waypoint.X += x_units
        self._waypoint.Y += y_units

        self._location.X += x_units
        self._location.Y += y_units

    def shift(self, direction: str, value: int):
        if direction == 'N':
            self._waypoint.Y += value
        elif direction == 'E':
            self._waypoint.X += value
        elif direction == 'S':
            self._waypoint.Y -= value
        elif direction == 'W':
            self._waypoint.X -= value


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        instructions = [row.strip() for row in f.readlines()]

    titanic = Titanic()
    for instruction in instructions:
        titanic.action(instruction)
    print(f'Part 1: {titanic.location.manhattan_distance_from_origin}')

    ghost = Ghost(waypoint=Coordinate(10, 1))
    for instruction in instructions:
        ghost.action(instruction)
    print(f'Part 2: {ghost.location.manhattan_distance_from_origin}')
