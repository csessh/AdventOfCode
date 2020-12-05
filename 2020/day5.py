#!/Users/thangdo/Documents/dev/csessh/bin/python

import math


class BoardingPass:
    def __init__(self, code: str):
        self._row_code = code[:-3]
        self._col_code = code[-3:]
        self._row = None
        self._col = None

    @property
    def ID(self) -> int:
        return self._row * 8 + self._col

    def process(self):
        possible_range = [0, 127]
        for direction in self._row_code:
            if direction == 'B':
                possible_range[0] = math.ceil((possible_range[0] + possible_range[1]) / 2)
            elif direction == 'F':
                possible_range[1] = math.floor((possible_range[0] + possible_range[1]) / 2)

            if possible_range[0] == possible_range[1]:
               self._row = possible_range[0]

        possible_range = [0, 7]
        for direction in self._col_code:
            if direction == 'R':
                possible_range[0] = math.ceil((possible_range[0] + possible_range[1]) / 2)
            elif direction == 'L':
                possible_range[1] = math.floor((possible_range[0] + possible_range[1]) / 2)

            if possible_range[0] == possible_range[1]:
               self._col = possible_range[0]


with open('test.txt', 'r') as f:
    boarding_passes = f.readlines()


def solve_part1():
    VIP = 0
    for bp in boarding_passes:
        ticket = BoardingPass(bp.strip())
        ticket.process()
        if ticket.ID > VIP:
            VIP = ticket.ID
    print(VIP)


def solve_part2():
    available_seats = []
    for bp in boarding_passes:
        ticket = BoardingPass(bp.strip())
        ticket.process()
        available_seats.append(ticket.ID)

    available_seats = sorted(available_seats)
    print(set(range(available_seats[0], available_seats[-1])) - set(available_seats))


solve_part1()
solve_part2()
