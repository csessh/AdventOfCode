import argparse
import numpy
import math
from queue import Queue
from typing import List, NamedTuple


class Location(NamedTuple):
    height: int
    row: int
    col: int


def get_lowest_points(terrain: List[List[int]]) -> list[Location]:
    width = len(terrain[0])
    depth = len(terrain)
    points = []

    for r, row in enumerate(terrain):
        for c, height in enumerate(row):
            validity = [
                height < terrain[r][c+1] if c+1 < width else True,
                height < terrain[r][c-1] if c-1 >= 0 else True,
                height < terrain[r+1][c] if r+1 < depth else True,
                height < terrain[r-1][c] if r-1 >= 0 else True
            ]

            if all(validity):
                points.append(Location(height, r, c))
    return points


def get_largest_basins(lowest_points: List[Location], terrain: List[List[int]], top: int=3) -> List[int]:
    width = len(terrain[0])
    depth = len(terrain)
    basins = []

    for location in lowest_points:
        visited = set()
        scout = Queue()
        scout.put(location)

        while not scout.empty():
            location = scout.get()

            if location.height == 9:
                continue

            if (location.row, location.col) in visited:
                continue

            visited.add((location.row, location.col))

            # Eastern neighbour
            if location.col+1 < width:
                adjacent_val = terrain[location.row][location.col+1]
                if adjacent_val > location.height:
                    scout.put(
                        Location(
                            height=adjacent_val,
                            row=location.row,
                            col=location.col+1
                        )
                    )

            # Western neighbour
            if location.col-1 >= 0:
                adjacent_val = terrain[location.row][location.col-1]
                if adjacent_val > location.height:
                    scout.put(
                        Location(
                            height=adjacent_val,
                            row=location.row,
                            col=location.col-1
                        )
                    )

            # Souther neighbour
            if location.row+1 < depth:
                adjacent_val = terrain[location.row+1][location.col]
                if adjacent_val > location.height:
                    scout.put(
                        Location(
                            height=adjacent_val,
                            row=location.row+1,
                            col=location.col
                        )
                    )

            # Northern neighbour
            if location.row-1 >= 0:
                adjacent_val = terrain[location.row-1][location.col]
                if adjacent_val > location.height:
                    scout.put(
                        Location(
                            height=adjacent_val,
                            row=location.row-1,
                            col=location.col
                        )
                    )

        basins.append(len(visited))
    return sorted(basins)[-top:]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        terrain = numpy.array(
            [
                list(map(int, list(val.strip())))
                for val in [line for line in f.readlines()]
            ]
        )

    points = get_lowest_points(terrain)
    basins = get_largest_basins(points, terrain)

    if args.test:
        assert sum([x.height+1 for x in points]) == 15
        assert math.prod(basins) == 1134
    else:
        print(f'Part 1: {sum([x.height+1 for x in points])}')
        print(f'Part 2: {math.prod(basins)}')