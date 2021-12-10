import argparse
import numpy
import math
from typing import List, Dict, NamedTuple, Tuple


ILLEGAL_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

PAIRS = {
    '{': '}',
    '<': '>',
    '[': ']',
    '(': ')'
}


def is_completed(line: str) -> Tuple[int, List[str]]:
    openers = []

    for c in line:
        if PAIRS.get(c):
            openers.append(c)
        else:
            if PAIRS.get(openers[-1]) == c:
                openers.pop()
            else:
                return ILLEGAL_POINTS[c], None
    return 0, openers


def calculate_penalty(data: List[str]) -> Tuple[int, int]:
    penalty = 0
    scores = []
    for line in data:
        error, leftovers = is_completed(line)
        penalty += error

        if leftovers:
            score = 0

            for c in reversed(leftovers):
                score *= 5
                score += SCORE[PAIRS[c]]
            scores.append(score)
    return penalty, sorted(scores)[len(scores)//2]


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        data = numpy.array(
            [line.strip() for line in f.readlines()]
        )

    """
    sample -> [
        '[({(<(())[]>[[{[]{<()<>>'
        '[(()[<>])]({[<{<<[]>>('
        '{([(<{}[<>[]}>{[]{[(<()>'
        '(((({<>}<{<{<>}{[]{[]{}'
        '[[<[([]))<([[{}[[()]]]'
        '[{[{({}]{}}([{[{{{}}([]'
        '{<[[]]>}<{[{[{[]{()[[[]'
        '[<(<(<(<{}))><([]([]()'
        '<{([([[(<>()){}]>(<<{{'
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]
    """

    point, score = calculate_penalty(data)

    if args.test:
        assert point == 26397
        assert score == 288957
    else:
        print(f'Part 1: {point}')
        print(f'Part 2: {score}')
