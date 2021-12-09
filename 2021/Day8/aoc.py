import argparse
from typing import List, NamedTuple


"""
Seven-segment display:

    0:      1:      2:      3:      4:
     aaaa    ....    aaaa    aaaa    ....
    b    c  .    c  .    c  .    c  b    c
    b    c  .    c  .    c  .    c  b    c
     ....    ....    dddd    dddd    dddd
    e    f  .    f  e    .  .    f  .    f
    e    f  .    f  e    .  .    f  .    f
     gggg    ....    gggg    gggg    ....

    5:      6:      7:      8:      9:
     aaaa    aaaa    aaaa    aaaa    aaaa
    b    .  b    .  .    c  b    c  b    c
    b    .  b    .  .    c  b    c  b    c
     dddd    dddd    ....    dddd    dddd
    .    f  e    f  .    f  e    f  .    f
    .    f  e    f  .    f  e    f  .    f
     gggg    gggg    ....    gggg    gggg

"""


class Signal(NamedTuple):
    patterns: List[str]
    output: List[str]


def count_easy_digits_in_output(data: List[Signal]) -> int:
    count = 0
    for signal in data:
        _, output = signal

        for i in output:
            if len(i) in [2, 3, 4, 7]:
                count += 1

    return count


def get_sum_of_output(data: List[Signal]) -> int:
    output_sum = 0
    for signal in data:
        scrambler = {
            8: set('abcdefg')
        }

        patterns, output = signal
        for digit in patterns[:-1]:
            wires = set(digit)

            if len(digit) == 2:
                scrambler[1] = wires
            elif len(digit) == 3:
                scrambler[7] = wires
            elif len(digit) == 4:
                scrambler[4] = wires
            elif len(digit) == 5:
                #
                # This digit can be: [2 3 5]
                #
                if len(wires.intersection(scrambler[4])) == 2 and len(wires.intersection(scrambler[1])) == 1:
                    scrambler[2] = wires
                elif len(wires.intersection(scrambler[1])) == 2 and len(wires.intersection(scrambler[7])) == 3:
                    scrambler[3] = wires
                elif len(wires.intersection(scrambler[4])) == 3 and len(wires.intersection(scrambler[1])) == 1:
                    scrambler[5] = wires
            elif len(digit) == 6:
                #
                # This digit can be [0 6 9]
                #
                if len(wires.intersection(scrambler[1])) == 1 and len(wires.intersection(scrambler[5])) == 5:
                    scrambler[6] = wires
                elif len(wires.intersection(scrambler[1])) == 2 and len(wires.intersection(scrambler[5])) == 5:
                    scrambler[9] = wires
                elif len(wires.intersection(scrambler[8])) == 6:
                    scrambler[0] = wires

        result = ''
        for digit in output:
            for value, mapping in scrambler.items():
                if set(digit) == mapping:
                    result += str(value)

        output_sum += int(result)
    return output_sum


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    lines = []
    with open('test.txt' if not args.test else 'sample.txt') as f:
        data = [
            Signal(
                patterns=sorted(signal.strip().split(' '), key=lambda x: len(x)),
                output=output.strip().split(' ')
            )
            for signal, output in [
                part for part in [
                    line.strip().split('|') for line in f.readlines()
                ]
            ]
        ]

    if args.test:
        assert count_easy_digits_in_output(data) == 26
        assert get_sum_of_output(data) == 61229
    else:
        print(f'Part 1: {count_easy_digits_in_output(data)}')
        print(f'Part 2: {get_sum_of_output(data)}')