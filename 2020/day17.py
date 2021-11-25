from enum import Enum
from typing import List


class Status(str, Enum):
    Active = '#'
    Inactive = '.'


class ZAxis(Enum):
    FRONT = -1
    MID = 0
    BACK = 1


MAX_CYCLES = 6


def get_neighbours(X: int, y: int, z: int) -> List[str]:
    return []


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        cube = [[line.strip() for line in f.readlines()]] * len(ZAxis)


# https://www.geeksforgeeks.org/how-to-draw-3d-cube-using-matplotlib-in-python/