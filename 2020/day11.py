#!/Users/thangdo/Documents/dev/csessh/bin/python

from abc import abstractmethod
from copy import deepcopy
from typing import Tuple


FLOOR = '.'
OCCUPIED = '#'
EMPTY = 'L'
EDGE = 'X'


class Ferry:
    seats_map = None

    def __init__(self):
        self._provisioning = deepcopy(Ferry.seats_map)
        self._width = len(Ferry.seats_map[0])
        self._height = len(Ferry.seats_map)
        self._stablized = False
        self._seat_count = 0

    @staticmethod
    def print():
        for row in Ferry.seats_map:
            print(row)
        print()

    def update(self, tolerance=4):
        dirty = False
        for row in range(0, self._height):
            for seat in range(0, self._width):
                if Ferry.seats_map[row][seat] == FLOOR:
                    continue

                surroundings = self.get_surroundings((row, seat))
                if Ferry.seats_map[row][seat] == EMPTY:
                    if surroundings.count(OCCUPIED) == 0:
                        self._provisioning[row][seat] = OCCUPIED
                        self._seat_count += 1
                        dirty = True
                elif Ferry.seats_map[row][seat] == OCCUPIED:
                    if surroundings.count(OCCUPIED) >= tolerance:
                        self._provisioning[row][seat] = EMPTY
                        self._seat_count -= 1
                        dirty = True

        if dirty:
            Ferry.seats_map = deepcopy(self._provisioning)
        else:
            self._stablized = True

    @abstractmethod
    def get_surroundings(self, index: Tuple[int, int]) -> list:
        pass

    @property
    def stablized(self) -> bool:
        return self._stablized

    @property
    def seat_count(self) -> int:
        return self._seat_count


class Part1(Ferry):
    def get_surroundings(self, index: Tuple[int, int]) -> list:
        row, seat = index
        surroundings = [None] * 8
        surroundings[0] = Ferry.seats_map[row-1][seat-1] if row - 1 >= 0 and seat - 1 >= 0 else None
        surroundings[1] = Ferry.seats_map[row-1][seat] if row - 1 >= 0 else None
        surroundings[2] = Ferry.seats_map[row-1][seat+1] if row - 1 >= 0 and seat + 1 < self._width else None
        surroundings[3] = Ferry.seats_map[row][seat+1] if seat + 1 < self._width else None
        surroundings[4] = Ferry.seats_map[row+1][seat+1] if row + 1 < self._height and seat + 1 < self._width else None
        surroundings[5] = Ferry.seats_map[row+1][seat] if row + 1 < self._height else None
        surroundings[6] = Ferry.seats_map[row+1][seat-1] if row + 1 < self._height and seat - 1 >= 0 else None
        surroundings[7] = Ferry.seats_map[row][seat-1] if seat - 1 >= 0 else None
        return surroundings


class Part2(Ferry):
    def get_surroundings(self, index: Tuple[int, int]) -> list:
        row, seat = index
        surroundings = [None] * 8
        reach = 1
        while surroundings.count(None) > 0:
            if row-reach >= 0 and seat-reach >= 0 and surroundings[0] is None:
                if Ferry.seats_map[row-reach][seat-reach] != FLOOR:
                    surroundings[0] = Ferry.seats_map[row-reach][seat-reach]
            elif surroundings[0] is None:
                surroundings[0] = EDGE

            if row - reach >= 0 and not surroundings[1]:
                if Ferry.seats_map[row-reach][seat] != FLOOR:
                    surroundings[1] = Ferry.seats_map[row-reach][seat]
            elif surroundings[1] is None:
                surroundings[1] = EDGE

            if row - reach >= 0 and seat + reach < self._width and surroundings[2] is None:
                if Ferry.seats_map[row-reach][seat+reach] != FLOOR:
                    surroundings[2] = Ferry.seats_map[row-reach][seat+reach]
            elif surroundings[2] is None:
                surroundings[2] = EDGE

            if seat + reach < self._width and not surroundings[3]:
                if Ferry.seats_map[row][seat+reach] != FLOOR:
                    surroundings[3] = Ferry.seats_map[row][seat+reach]
            elif surroundings[3] is None:
                surroundings[3] = EDGE

            if row + reach < self._height and seat + reach < self._width and surroundings[4] is None:
                if Ferry.seats_map[row+reach][seat+reach] != FLOOR:
                    surroundings[4] = Ferry.seats_map[row+reach][seat+reach]
            elif surroundings[4] is None:
                surroundings[4] = EDGE

            if row + reach < self._height and surroundings[5] is None:
                if Ferry.seats_map[row+reach][seat] != FLOOR:
                    surroundings[5] = Ferry.seats_map[row+reach][seat]
            elif surroundings[5] is None:
                surroundings[5] = EDGE

            if row + reach < self._height and seat - reach >= 0 and surroundings[6] is None:
                if Ferry.seats_map[row+reach][seat-reach] != FLOOR:
                    surroundings[6] = Ferry.seats_map[row+reach][seat-reach]
            elif surroundings[6] is None:
                surroundings[6] = EDGE

            if seat - reach >= 0 and surroundings[7] is None:
                if Ferry.seats_map[row][seat-reach] != FLOOR:
                    surroundings[7] = Ferry.seats_map[row][seat-reach]
            elif surroundings[7] is None:
                surroundings[7] = EDGE

            reach += 1
        return surroundings


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        Ferry.seats_map = [list(row.strip()) for row in f.readlines()]

    # ferry = Part1()
    # while not ferry.stablized:
    #     ferry.update(tolerance=4)
    # print(ferry.seat_count)

    ferry = Part2()
    while not ferry.stablized:
        ferry.update(tolerance=5)
    print(ferry.seat_count)
