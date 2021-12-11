import argparse
import numpy
from queue import Queue
from enum import Enum
from typing import Dict, Tuple
from time import sleep


class Energy(int, Enum):
    EMPTY = 0
    FULL = 9


def draw(octopi: Dict[Tuple[int, int], int]):
    board = numpy.array([numpy.array(numpy.zeros(10))] * 10)

    for pos in octopi.keys():
        x, y = pos
        board[y][x] = octopi[pos]

    print(board)
    if numpy.sum(board) == 0:
        raise Exception


def count_flashes(octopi: Dict[Tuple[int, int], int], iteration: int) -> int:
    flash_count_at_iteration = 0
    bigbang = -1
    total_flashes = 0


    print('Starting positions')
    draw(octopi)

    step = 1
    while True:
        chain_reactions = Queue()
        flashed = {}


        for octopus in octopi.keys():
            octopi[octopus] += 1

            if octopi[octopus] > Energy.FULL:
                chain_reactions.put(octopus)
                flashed[octopus] = True
                total_flashes += 1

        while not chain_reactions.empty():
            octopus = chain_reactions.get()
            octopi[octopus] = 0
            x, y = octopus

            neighbours = [
                (x-1, y),
                (x+1, y),
                (x, y-1),
                (x, y+1),
                (x+1, y+1),
                (x-1, y-1),
                (x+1, y-1),
                (x-1, y+1)
            ]

            for n in neighbours:
                if octopi.get(n):
                    octopi[n] += 1

                    if octopi[n] > Energy.FULL and not flashed.get(n):
                        chain_reactions.put(n)
                        flashed[n] = True
                        total_flashes += 1


        if step == iteration:
            flash_count_at_iteration = total_flashes

        try:
            print(f'Iteration #{step}, {total_flashes} total flashes')
            draw(octopi)
            step += 1
            sleep(0.2)
        except Exception:
            bigbang = step
            break

    return flash_count_at_iteration, bigbang


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        data = {}
        for y, line in enumerate(f.readlines()):
            for x, value in enumerate(line.strip()):
                data[(x, y)] = int(value)

    flashes, bigbang = count_flashes(data, iteration=100)
    if args.test:
        assert flashes == 1656
        assert bigbang == 195
    else:
        print(f'Part 1: {flashes}')
        print(f'Part 2: {bigbang}')
