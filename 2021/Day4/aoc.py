import argparse
import numpy
from typing import List, NamedTuple


BOARD_SIZE = 5
Matrix = List[List[int]]


class Coordinate(NamedTuple):
    x: int
    y: int


class Board:
    def __init__(self, id: int, data: Matrix):
        self._id = id
        self._bingo = False
        self._raw = numpy.array(data)
        self._positions = {}

        for y, row in enumerate(data):
            for x, col in enumerate(row):
                pos = Coordinate(x=x, y=y)
                self._positions[col] = pos

    def mark(self, value: int):
        if value not in self._positions:
            return

        pos = self._positions[value]
        self._raw[pos.y][pos.x] += -999

        # check horizontal status
        self._bingo = (self._raw[pos.y] < 0).sum() == BOARD_SIZE
        if self._bingo == True:
            return

        # check vertical status
        self._bingo = (self._raw[:, pos.x] < 0).sum() == BOARD_SIZE
        if self._bingo == True:
            return

    @property
    def bingo(self) -> bool:
        return self._bingo

    @property
    def unmarked_sum(self) -> int:
        return numpy.where(self._raw > 0, self._raw, 0).sum()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        drawn_numbers = list(map(int, f.readline().strip().split(',')))
        f.readline()

        data_matrix = [
            numpy.array(list(map(int, line.strip().split())))
            for line in f.readlines()
            if len(line.strip()) > 0
        ]

    boards = [
        Board(i//BOARD_SIZE, data_matrix[i:i+BOARD_SIZE])
        for i in range(0, len(data_matrix), BOARD_SIZE)
    ]

    first_score = None
    last_score = None
    winners = []
    for n in drawn_numbers:
        for idx, board in enumerate(boards):
            if idx in winners:
                continue

            board.mark(n)
            if board.bingo:
                winners.append(idx)
                last_score = board.unmarked_sum * n

                if not first_score:
                    first_score = last_score

                    if args.test:
                        assert first_score == 4512
                    print(f'Part 1: {first_score}')

    if args.test:
        assert last_score == 1924
    print(f'part 2: {last_score}')