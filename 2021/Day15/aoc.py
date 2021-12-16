import argparse
import numpy
from math import inf
from queue import PriorityQueue
from typing import List


def dijkstra(grid: List[List[int]]) -> int:
    height = len(grid)
    width = len(grid[0])
    risks = numpy.full((height, width), inf)
    risks[0][0] = 0

    point = (0, 0)
    seen = {}

    scout = PriorityQueue()
    scout.put((0, point))

    while not scout.empty():
        risk, point = scout.get()
        seen[point] = True

        x, y = point
        neighbours = [
            (x-1, y), # Left
            (x+1, y), # Right
            (x, y-1), # Up
            (x, y+1)  # Down
        ]

        for neighbour in neighbours:
            xi, yi = neighbour
            if 0 <= xi < height and 0 <= yi < width:
                if not seen.get((xi, yi)):
                    if risk + grid[xi][yi] < risks[xi][yi]:
                        risks[xi][yi] = risk + grid[xi][yi]

                        scout.put(
                            (risks[xi][yi], (xi, yi))
                        )

    """
    calculated risks to travel to each position in the grid:
        [[ 0.  1.  7. 10. 17. 22. 23. 30. 34. 36.]
        [ 1.  4. 12. 11. 14. 21. 23. 29. 32. 34.]
        [ 3.  4.  7. 13. 18. 19. 20. 23. 25. 33.]
        [ 6. 10. 16. 17. 26. 22. 21. 26. 31. 38.]
        [13. 14. 20. 20. 24. 23. 28. 27. 28. 29.]
        [14. 17. 18. 27. 25. 25. 33. 28. 31. 36.]
        [15. 18. 23. 32. 34. 26. 28. 32. 33. 34.]
        [18. 19. 21. 26. 30. 28. 29. 35. 36. 43.]
        [19. 21. 30. 29. 30. 31. 37. 40. 38. 39.]
        [21. 24. 25. 26. 35. 35. 39. 44. 46. 40.]]
    """
    return int(risks[-1][-1])


def expand(grid: List[List[int]]) -> List[List[int]]:
    bigger_grid = []

    for i in range(5):
        for r in range(grid.shape[0]):
            new_array = []
            for k in range(5):
                new_array += [i+j+k if i+j+k <=9 else (i+j+k)%9 for j in grid[r]]
            bigger_grid.append(new_array)

    return bigger_grid


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        grid = numpy.array([
            list(map(int, list(line.strip())))
            for line in f.readlines()
        ])

    massive_grid = expand(grid)

    small_grid_risk = dijkstra(grid)
    big_grid_risk = dijkstra(massive_grid)

    if args.test:
        assert small_grid_risk == 40
        assert big_grid_risk == 315

    print(f'Part 1: {small_grid_risk}')
    print(f'Part 2: {big_grid_risk}')
