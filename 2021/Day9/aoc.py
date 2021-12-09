import argparse
import numpy
import math
from queue import Queue
from typing import List, NamedTuple


class Point(NamedTuple):
    value: int
    row: int
    col: int


def get_lowest_points(data: List[List[int]]) -> list[Point]:
    width = len(data[0])
    depth = len(data)
    points = []

    for r, row in enumerate(data):
        for c, val in enumerate(row):
            validity = [
                val < data[r][c+1] if c+1 < width else True,
                val < data[r][c-1] if c-1 >= 0 else True,
                val < data[r+1][c] if r+1 < depth else True,
                val < data[r-1][c] if r-1 >= 0 else True
            ]

            if False not in validity:
                points.append(Point(val, r, c))
    return points


def get_largest_basins(lowest_points: List[Point], data: List[List[int]], top: int=3) -> List[int]:
    width = len(data[0])
    depth = len(data)
    basins = []

    for point in lowest_points:
        visited = set()

        scout = Queue()
        scout.put(point)

        while not scout.empty():
            location = scout.get()

            if location.value == 9:
                continue

            if (location.row, location.col) in visited:
                continue

            visited.add((location.row, location.col))

            if location.col+1 < width:
                adjacent_val = data[location.row][location.col+1]
                if adjacent_val > location.value:
                    loc = Point(
                        value=adjacent_val,
                        row=location.row,
                        col=location.col+1
                    )

                    scout.put(loc)

            if location.col-1 >= 0:
                adjacent_val = data[location.row][location.col-1]
                if adjacent_val > location.value:
                    loc = Point(
                        value=adjacent_val,
                        row=location.row,
                        col=location.col-1
                    )

                    scout.put(loc)

            if location.row+1 < depth:
                adjacent_val = data[location.row+1][location.col]
                if adjacent_val > location.value:
                    loc = Point(
                        value=adjacent_val,
                        row=location.row+1,
                        col=location.col
                    )

                    scout.put(loc)

            if location.row-1 >= 0:
                adjacent_val = data[location.row-1][location.col]
                if adjacent_val > location.value:
                    loc = Point(
                        value=adjacent_val,
                        row=location.row-1,
                        col=location.col
                    )

                    scout.put(loc)

        basins.append(len(visited))
    return sorted(basins)[-top:]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    lines = []
    with open('test.txt' if not args.test else 'sample.txt') as f:
        data = numpy.array(
            [
                list(map(int, list(val.strip())))
                for val in [line for line in f.readlines()]
            ]
        )

    points = get_lowest_points(data)
    basins = get_largest_basins(points, data)

    if args.test:
        assert sum([x.value+1 for x in points]) == 15
        assert math.prod(basins) == 1134
    else:
        print(f'Part 1: {sum([x.value+1 for x in points])}')
        print(f'Part 2: {math.prod(basins)}')