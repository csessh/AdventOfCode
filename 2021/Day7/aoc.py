import argparse
import numpy
from typing import List


def calculate_cost_of_stepping(cost: int, expense: int=0) -> int:
    if expense == 0:
        return cost

    return sum(numpy.arange(cost+1))


def calculate_the_least_amount_of_fuel(crabs: List[int], cost: int=0) -> int:
    min = numpy.min(crabs)
    max = numpy.max(crabs)

    most_effective = None
    for i in range(min, max+1):
        fuel = sum([calculate_cost_of_stepping(abs(x - i), cost) for x in crabs])
        if most_effective is None or fuel < most_effective:
            most_effective = fuel

    return most_effective


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    lines = []
    with open('test.txt' if not args.test else 'sample.txt') as f:
        crabs = numpy.array(
            list(map(int, f.readline().strip().split(',')))
        )

    if args.test:
        assert calculate_the_least_amount_of_fuel(crabs) == 37
        assert calculate_the_least_amount_of_fuel(crabs, cost=1) == 168
    else:
        print(f'Part 1: {calculate_the_least_amount_of_fuel(crabs)}')
        print(f'Part 2: {calculate_the_least_amount_of_fuel(crabs, cost=1)}')