#!/Users/thangdo/Documents/dev/csessh/bin/python

import math

class BoardingPass:
    def __init__(self, code: str):
        self._row_code = code[:-3]
        self._col_code = code[-3:]
        self._translation = str.maketrans('LRBF', '0110')
        self._row = int(self._row_code.translate(self._translation), 2)
        self._col = int(self._col_code.translate(self._translation), 2)

    @property
    def ID(self) -> int:
        return self._row * 8 + self._col


with open('test.txt', 'r') as f:
    boarding_passes = f.readlines()


def solve_part1():
    VIP = 0
    for bp in boarding_passes:
        ticket = BoardingPass(bp.strip())
        if ticket.ID > VIP:
            VIP = ticket.ID
    print(VIP)


def solve_part2():
    available_seats = []
    for bp in boarding_passes:
        ticket = BoardingPass(bp.strip())
        available_seats.append(ticket.ID)

    available_seats = sorted(available_seats)
    print(set(range(available_seats[0], available_seats[-1])) - set(available_seats))


solve_part1()
solve_part2()
