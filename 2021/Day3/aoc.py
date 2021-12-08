import argparse
import numpy
from collections import Counter
from typing import List, Tuple


def get_O2_rating(data: List[List[int]]) -> int:
    rating = ''
    for index in range(len(data)):
        counter = Counter(data[index]).most_common()
        most_common = counter[0]

        if len(counter) > 1:
            least_common = counter[1]
            if most_common[1] == least_common[1] and most_common[0] == 0:
                most_common, least_common = least_common, most_common

        rating += str(most_common[0])
        valid_column_indices = numpy.where(data[index] != most_common[0])
        data = numpy.delete(data, list(valid_column_indices), 1)

    return int(rating, 2)


def get_CO2_rating(data: List[List[int]]) -> int:
    rating = ''
    for index in range(len(data)):
        counter = Counter(data[index]).most_common()
        most_common = counter[0]

        if len(counter) > 1:
            least_common = counter[1]
            if most_common[1] == least_common[1] and most_common[0] == 0:
                most_common, least_common = least_common, most_common

            least_common_bit = 0 if most_common[0] == 1 else 1
        else:
            least_common_bit = most_common[0]

        rating += str(least_common_bit)
        valid_column_indices = numpy.where(data[index] != least_common_bit)
        data = numpy.delete(data, list(valid_column_indices), 1)

    return int(rating, 2)


def get_power_consumption(data: List[List[int]]) -> Tuple[int, int]:
    gamma = ''
    epsilon = ''
    for bits in rotated_data:
        counter = Counter(bits).most_common()
        most_common = counter[0]
        bit, _ = most_common
        gamma += str(bit)

        try:
            least_common = counter[1]
            bit, _ = least_common
        except:
            if bit == 0:
                bit = 1
        finally:
            epsilon += str(bit)

    return int(gamma, 2), int(epsilon, 2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        """
            original:
                [0 0 1 0 0]
                [1 1 1 1 0]
                [1 0 1 1 0]
                [1 0 1 1 1]
                [1 0 1 0 1]
                [0 1 1 1 1]
                [0 0 1 1 1]
                [1 1 1 0 0]
                [1 0 0 0 0]
                [1 1 0 0 1]
                [0 0 0 1 0]
                [0 1 0 1 0]

            Rotated:
                [0 0 1 1 1 0 0 1 1 1 1 0]
                [1 0 1 0 1 0 1 0 0 0 1 0]
                [0 0 0 0 1 1 1 1 1 1 1 1]
                [1 1 0 0 0 1 1 0 1 1 1 0]
                [0 0 1 0 0 1 1 1 1 0 0 0]
        """
        data = numpy.array([
            list(map(int, list(line.strip())))
            for line in f.readlines()
        ])
        rotated_data = numpy.rot90(data, k=1, axes=(1,0))

    #
    # Part 1
    #
    gamma, epsilon = get_power_consumption(rotated_data)

    if args.test:
        assert gamma * epsilon == 198
    print(f'Submarine\'s power consumption = {gamma * epsilon}')

    #
    # Part 2
    #
    oxygen = get_O2_rating(rotated_data)
    carbon_dioxide = get_CO2_rating(rotated_data)

    if args.test:
        assert carbon_dioxide * oxygen == 230
    print(f'Submarine\'s life support rating = {carbon_dioxide * oxygen}')
