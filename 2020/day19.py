import queue
import re
from queue import Queue
from typing import List, Set, Dict


RULE_PATTERNS = r'([0-9]+): (?:([0-9]+ [0-9]+(?:\s*\|*\s*[0-9]+ [0-9]+)*)|(?:\"([a-z]+)\"))'


def construct_possible_matches(rules):
    """
        {
            0: [[4, 1]],
            1: [[2, 3], [3, 2]],
            2: [[4, 4], [5, 5]],
            3: [[4, 5], [5, 4]],
            4: 'a',
            5: 'b'
        }
    """
    matches = {}


    return matches


if __name__ == '__main__':
    with open('test.txt') as f:
        rules = {}

        # Parse rules
        while True:
            rule = f.readline().strip()
            if rule == '':
                break

            """
                regex match groups ->
                    ('0', '4 1', None)
                    ('1', '2 3 | 3 2', None)
                    ('2', '4 4 | 5 5', None)
                    ('3', '4 5 | 5 4', None)
                    ('4', None, 'a')
                    ('5', None, 'b')

                converted to a dictionary -> {
                    0: [[4, 1]],
                    1: [[2, 3], [3, 2]],
                    2: [[4, 4], [5, 5]],
                    3: [[4, 5], [5, 4]],
                    4: 'a',
                    5: 'b'
                }
            """
            match = re.match(RULE_PATTERNS, rule)
            if match.groups()[1]:
                rules[int(match.groups()[0])] = [
                    list(map(int, x.strip().split(' '))) for x in
                    match.groups()[1].split('|')
                ]
            else:
                rules[int(match.groups()[0])] = match.groups()[2]

        # Parse messages
        messages = set([line.strip() for line in f.readlines()])

        #
        # Part 1
        #
        possible_matches = construct_possible_matches(rules)
        matches = messages.intersection(possible_matches)
        print(f'Part 1: {len(matches)}')

        #
        # Part 2
        #