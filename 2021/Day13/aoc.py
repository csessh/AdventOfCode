import argparse
import numpy
import os
from time import sleep
from typing import List


def draw(grid: List[List[bool]]):
    os.system("clear" if os.name == "posix" else "cls")

    for _, row in enumerate(grid):
        for _, dot in enumerate(row):
            if dot:
                print("\u2588", end="")
            else:
                print(" ", end="")
        print()
    sleep(1)


def fold_up(grid: List[List[bool]], crease: int):
    top = grid[:crease]
    bottom = grid[crease + 1 :]
    bottom = numpy.flip(bottom, 0)
    grid = (top + bottom).astype(bool)

    draw(grid)
    return grid


def fold_left(grid: List[List[bool]], crease: int):
    left = grid[:, :crease]
    right = grid[:, crease + 1 :]
    right = numpy.flip(right, 1)
    grid = (left + right).astype(bool)

    draw(grid)
    return grid


if __name__ == "__main__":
    parser = argparse.ArgumentParser("AoC")
    parser.add_argument(
        "-t", "--test", help="Run sample input and verify answers", action="store_true"
    )
    args = parser.parse_args()

    dots = []
    folds = []

    with open("test.txt" if not args.test else "sample.txt") as f:
        width = 0
        height = 0

        while True:
            position = f.readline().strip()
            if len(position) == 0:
                break

            x, y = list(map(int, position.strip().split(",")))
            dots.append((x, y))

            if x > width:
                width = x

            if y > height:
                height = y

        folds = [
            (axis, int(index))
            for axis, index in [
                line.strip()[len("fold along ") :].split("=") for line in f.readlines()
            ]
        ]

    grid = numpy.zeros((height + 1, width + 1), dtype=bool)
    for dot in dots:
        x, y = dot
        grid[y][x] = True

    draw(grid)
    first_fold_visibile_dots = 0

    for i, crease in enumerate(folds):
        axis, idx = crease
        if axis == "y":
            grid = fold_up(grid, idx)
        elif axis == "x":
            grid = fold_left(grid, idx)

        if i == 0:
            first_fold_visibile_dots = numpy.sum(grid)

    if args.test:
        assert first_fold_visibile_dots == 17

    print(f"{first_fold_visibile_dots} visible dots after 1 fold")
    print(f"{numpy.sum(grid)} visible dots after {len(folds)} folds")
