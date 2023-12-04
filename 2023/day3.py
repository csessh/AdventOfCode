import re
from dataclasses import dataclass
from typing import Tuple, List, Dict


@dataclass()
class Number:
    value: int
    row: int
    span: Tuple[int, int]


@dataclass()
class Symbol:
    value: str
    row: int
    col: int


if __name__ == '__main__':
    with open('input/day3', 'r') as f:
        data = f.readlines()

    all_the_numbers: List[Number] = []
    all_the_symbols: List[Symbol] = []
    symbols_pos_lookup: Dict[Tuple[int,int], Symbol] = {}
    numbers_pos_lookup: Dict[Tuple[int,int], Number] = {}

    # San
    for row, line in enumerate(data):
        numbers = re.finditer(r'\d+', line)
        symbols = re.finditer(r'(?!\d|\.).', line)

        for number in numbers:
            n = Number(
                value=int(number.group(0)),
                row=row,
                span=number.span()
            )

            for i in range(number.span()[0], number.span()[1]):
                numbers_pos_lookup[(i, n.row)] = n
            all_the_numbers.append(n)

        for sym in symbols:
            s = Symbol(
                value=sym.group(0),
                row=row,
                col=sym.span()[0]
            )
            symbols_pos_lookup[(s.col, s.row)] = s
            all_the_symbols.append(s)

    # Part 1
    part_numbers_total = 0
    for number in all_the_numbers:
        # Look one row above
        row = number.row - 1
        for i in range(number.span[0]-1, number.span[1]+1):
            if (i, row) in symbols_pos_lookup:
                part_numbers_total += number.value
                break

        # Look one row below
        row = number.row + 1
        for i in range(number.span[0]-1, number.span[1]+1):
            if (i, row) in symbols_pos_lookup:
                part_numbers_total += number.value
                break

        # Look left
        if (number.span[0]-1, number.row) in symbols_pos_lookup:
            part_numbers_total += number.value
            continue

        # Look right
        if (number.span[1], number.row) in symbols_pos_lookup:
            part_numbers_total += number.value
            continue

    # Part 2
    gear_ratio_total = 0
    for symbol in all_the_symbols:
        if symbol.value != '*':
            continue

        seen = []

        # Look one row above
        for i in range(symbol.col-1, symbol.col+2):
            if (i, symbol.row - 1) in numbers_pos_lookup:
                if numbers_pos_lookup[(i, symbol.row - 1)] not in seen:
                    seen.append(numbers_pos_lookup[(i, symbol.row - 1)])

        # Look one row below
        for i in range(symbol.col-1, symbol.col+2):
            if (i, symbol.row + 1) in numbers_pos_lookup:
                if numbers_pos_lookup[(i, symbol.row + 1)] not in seen:
                    seen.append(numbers_pos_lookup[(i, symbol.row + 1)])

        # Look left
        if (symbol.col - 1, symbol.row) in numbers_pos_lookup:
            seen.append(numbers_pos_lookup[(symbol.col-1, symbol.row)])

        # Look right
        if (symbol.col + 1, symbol.row) in numbers_pos_lookup:
            seen.append(numbers_pos_lookup[(symbol.col+1, symbol.row)])

        if len(seen) == 2:
            gear_ratio_total += seen[0].value * seen[1].value
            print(f'({symbol.col},{symbol.row}) gear sees {seen[0].value} and {seen[1].value} --> {seen[0].value * seen[1].value}')

    print(part_numbers_total)
    print(gear_ratio_total)
..........
...*......
.35.633...
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..