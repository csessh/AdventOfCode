import argparse
from enum import Enum


class Direction(str, Enum):
    UP = 'up'
    DOWN = 'down'
    FORWARD = 'forward'


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        data = [line.strip().split(' ') for line in f.readlines()]

    # Part 1
    x = y = 0
    for instruction in data:
        direction, val = instruction
        if direction == Direction.FORWARD:
            x += int(val)

        if direction == Direction.DOWN:
            y += int(val)

        if direction == Direction.UP:
            y -= int(val)

    if args.test:
        assert x*y == 150

    print(f'Part 1: {x*y}')

    # Part 2
    x = y = aim = 0
    for instruction in data:
        direction, val = instruction
        if direction == Direction.FORWARD:
            x += int(val)
            y += aim*int(val)

        if direction == Direction.DOWN:
            aim += int(val)

        if direction == Direction.UP:
            aim -= int(val)

    if args.test:
        assert x*y == 900

    print(f'Part 2: {x*y}')