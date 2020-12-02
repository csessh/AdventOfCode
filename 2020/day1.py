#!/Users/thangdo/Documents/dev/csessh/bin/python
from typing import Tuple


def read() -> set:
    with open('test.txt') as f:
        temp = f.readlines()
        data = set(list(map(int, temp)))
    return data

def solve_part1(numbers: set, target: int=2020) -> Tuple[int, int]:
    """
    Part 1: Target is set to 2020, we look for 2 numbers that add up to target
    """
    for number in numbers:
        the_other_half = target - number
        if the_other_half in numbers:
            return the_other_half, number
    return None, None

def solve_part2(numbers: set, target: int=2020) -> Tuple[int, int, int]:
    """
    Part 2: Target is set to 2020, we look for 3 numbers that add up to target
    """
    for x in numbers:
        sub_target = target - x
        y, z = solve_part1(numbers, sub_target)
        if y and z:
            return(x, y, z)
    return None, None, None


if __name__ == '__main__':
    numbers = read()
    a, b = solve_part1(numbers)
    print(a, b, a*b)

    x, y, z = solve_part2(numbers)
    print(x, y, z, x*y*z)