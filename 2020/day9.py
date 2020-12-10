#!/Users/thangdo/Documents/dev/csessh/bin/python

from itertools import combinations
from typing import Tuple
from day1 import find_combo_of_2


PREAMBLE_OFFSET = 25


with open('test.txt', 'r') as f:
    data = [int(x) for x in f.readlines()]


def find_weakness(numbers: list):
    weakness = None
    for index, number in enumerate(numbers[PREAMBLE_OFFSET:]):
        preambes = numbers[index:index+PREAMBLE_OFFSET]

        a, b = find_combo_of_2(preambes, number)
        if not a and not b:
            weakness = number
            break
    return weakness


def find_contigous_set_of_numbers(target: int) -> Tuple[int, int]:
    contigous_set = []
    for number in data:
        if sum(contigous_set) >= target:
            for i in range(len(contigous_set)):
                if sum(contigous_set[i:]) == target and len(contigous_set[i:]) > 1:
                    return (min(contigous_set[i:]), max(contigous_set[i:]))
            del contigous_set[0]
            contigous_set.append(number)
        elif sum(contigous_set) < target:
            contigous_set.append(number)


# Part 1
weakness = find_weakness(data)
print(weakness)

# Part 2
a, b = find_contigous_set_of_numbers(weakness)
print(a+b)