from copy import deepcopy
from enum import Enum
from typing import List, Tuple


class Status(str, Enum):
    Active = '#'
    Inactive = '.'


class ZAxis(int, Enum):
    FRONT = 0
    MID = 1
    BACK = 2


MAX_CYCLES = 6


class Cube:
    def __init__(self, slice: List[List[str]]):
        self._cube = [slice] * len(ZAxis)
        self._x = len(self._cube[0][0])
        self._y = len(self._cube[0])
        self._z = len(ZAxis)
        self._ref = None

    def transform(self):
        self._ref = deepcopy(self._cube)

        for z, slice in enumerate(self._cube):
            for x, row in enumerate(slice):
                for y, _ in enumerate(row):
                    cube = self._cube[z][y][x]
                    count = self._get_active_neighbours(x, y, z)

                    if cube == Status.Active:
                        if count not in [2, 3]:
                            cube = Status.Inactive
                    elif cube == Status.Inactive:
                        if count == 3:
                            cube = Status.Active

    def show(self, cycle: int=None):
        if cycle:
            print(f'Current cycle: {cycle}')

        for row in range(len(self._cube[0])):
            print(f'{self._cube[ZAxis.FRONT][row]}\t{self._cube[ZAxis.MID][row]}\t{self._cube[ZAxis.BACK][row]}')
        print()

    def _get_active_neighbours(self, x: int, y: int, z: int) -> Tuple[int, int]:
        actives = 0

        min_z = z-1 if z > 0 else z
        max_z = z+1 if z < self._z else z

        min_y = y-1 if y > 0 else y
        max_y = y+1 if y < self._y else y

        min_x = x-1 if x > 0 else x
        max_x = x+1 if x < self._x else x

        return actives


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        slice = [list(line.strip()) for line in f.readlines()]
        cube = Cube(slice)
        cube.show()

    for cycle in range(MAX_CYCLES):
        cube.transform()
        cube.show(cycle+1)