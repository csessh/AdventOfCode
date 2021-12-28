import argparse
import math
import re
from typing import List, Match


PAIR                  = re.compile(r'\[(\d+),(\d+)\]')
DOUBLE_DIGIT_NUMBER   = re.compile(r'\d\d+')
SINGLE_NUMBER         = re.compile(r'\d+')
IMMEDIATE_LEFT_NUMBER = re.compile(r'\d+(?!.*\d)')


def reduce(number: str) -> List:
    while True:
        #
        # Deal with explosion first
        #
        exploded = False
        for pair in PAIR.finditer(number):
            left = number[:pair.start()]
            if left.count('[') - left.count(']') >= 4:
                def add_left(match: Match[str]) -> str:
                    return str(int(match[0]) + int(pair[1]))

                def add_right(match: Match[str]) -> str:
                    return str(int(match[0]) + int(pair[2]))

                start = IMMEDIATE_LEFT_NUMBER.sub(add_left, number[:pair.start()], count=1)
                end = SINGLE_NUMBER.sub(add_right, number[pair.end():], count=1)
                number = f'{start}0{end}'

                exploded = True
                break

        if exploded:
            continue

        #
        # Splitting comes after explosions
        #
        splits = DOUBLE_DIGIT_NUMBER.search(number)
        if splits:
            def match_cb(match: Match[str]) -> str:
                left = math.floor(int(match[0])/2)
                right = math.ceil(int(match[0])/2)
                return f'[{left},{right}]'

            number = DOUBLE_DIGIT_NUMBER.sub(match_cb, number, count=1)
            continue

        return number


def calculate(number: List) -> int:
    if type(number) is int:
        return number
    return 3*calculate(number[0]) + 2*calculate(number[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        snailfish_numbers = [line.strip() for line in f.readlines()]

    result = snailfish_numbers[0]
    for num in snailfish_numbers[1:]:
        result = reduce(f'[{result},{num}]')

    magnitude = calculate(eval(result))

    maximum = 0
    for i, number in enumerate(snailfish_numbers):
        for other in snailfish_numbers[i+1:]:
            val = eval(reduce(f'[{number},{other}]'))
            maximum = max(maximum, calculate(val))

            val = eval(reduce(f'[{other},{number}]'))
            maximum = max(maximum, calculate(val))

    if args.test:
        assert magnitude == 4140
        assert calculate(eval('[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]')) == 4140
        assert calculate(eval('[[1,2],[[3,4],5]]')) == 143
        assert calculate(eval('[[[[1,1],[2,2]],[3,3]],[4,4]]')) == 445
        assert calculate(eval('[[[[3,0],[5,3]],[4,4]],[5,5]]')) == 791
        assert calculate(eval('[[[[5,0],[7,4]],[5,5]],[6,6]]')) == 1137
        assert calculate(eval('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]')) == 3488
        assert maximum == 3993

    print(f'Part 1: {magnitude}')
    print(f'Part 2: {maximum}')