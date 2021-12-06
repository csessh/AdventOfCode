import argparse
import numpy
import pandas
from collections import defaultdict
from typing import Dict


RESET = 6
MIN = 0


def count_lanternfish(days: int, school: Dict[int, int]) -> int:
    for _ in range(days):
        reset = school[MIN]
        for i in range(8):
            school[i], school[i+1] = school[i+1], school[i]
        school[RESET] += reset
    return sum(school.values())


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    lines = []
    with open('test.txt' if not args.test else 'sample.txt') as f:
        school_of_fish = numpy.array(
            list(
                map(int, f.readline().strip().split(','))
            )
        )

    if args.test:
        fish_tracker = defaultdict(int, pandas.value_counts(school_of_fish))
        assert count_lanternfish(80, fish_tracker) == 5934

        fish_tracker = defaultdict(int, pandas.value_counts(school_of_fish))
        assert count_lanternfish(256, fish_tracker) == 26984457539
    else:
        # Part 1
        fish_tracker = defaultdict(int, pandas.value_counts(school_of_fish))
        print(f'Part 1: Population after 80 days: {count_lanternfish(80, fish_tracker)}')

        # Part 2
        fish_tracker = defaultdict(int, pandas.value_counts(school_of_fish))
        print(f'Part 2: Population after 256 days: {count_lanternfish(256, fish_tracker)}')