from heapq import heappop, heappush
from typing import List, Tuple


def get_neighbours(grid: List[str], position: Tuple[int, int]):
    row, col = position

    try:
        if col - 1 < 0:
            raise IndexError

        north = row, col-1
    except IndexError:
        north = None

    try:
        if col + 1 >= len(grid[0]):
            raise IndexError

        south = row, col+1
    except IndexError:
        south = None

    try:
        if row + 1 >= len(grid):
            raise IndexError

        east = row+1, col
    except IndexError:
        east = None

    try:
        if row - 1 < 0:
            raise IndexError

        west = row-1, col
    except IndexError:
        west = None

    return north, south, east, west


def search(grid: List[str], start: Tuple[int, int]):
    seen = set()
    queue = [
        (0, start)
    ]

    while queue:
        distant, loc = heappop(queue)
        row, col = loc

        if loc not in seen:
            seen.add(loc)

            if grid[row][col] == 'E':
                return distant

            for neighbour in get_neighbours(grid, loc):
                if neighbour and neighbour not in seen:
                    n_row, n_col = neighbour

                    loc_height = ord(grid[row][col])
                    neighbour_height = ord(grid[n_row][n_col])

                    if (grid[n_row][n_col] == 'E'):
                        neighbour_height = ord('z')

                    if loc_height >= neighbour_height or neighbour_height - loc_height == 1 or loc == start:
                        heappush(queue, (distant+1, neighbour))

    return float("inf")


if __name__ == "__main__":
    grid = []
    row = col = 0
    start = end = None

    with open('input/day12') as f:
        for line in f.readlines():
            grid.append(line.strip())

            if 'S' in line:
                col = line.find('S')
                start = row, col

            if 'E' in line:
                col = line.find('E')
                end = row, col

            row+=1

    print(f'From {start} --> {end}\n')

    result = search(grid, start)
    shortest = result
    print(f'\nPart 1: distant from S to E: {result}')

    for idx, _ in enumerate(grid):
        result = search(grid, (idx, 0))

        if result < shortest:
            shortest = result

    print(f'\nPart 2: Shortest distant to E: {shortest}')

