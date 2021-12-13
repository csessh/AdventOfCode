import argparse
from typing import List, Dict, NamedTuple, Set


def walk(network, seen, cave, count):
    if cave.islower():
        seen[cave] = True

    if cave == 'end':
        count[0] += 1
    else:
        for neighbour in network.get(cave, []):
            if not seen.get(neighbour):
                walk(network, seen, neighbour, count)

    seen[cave] = False


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    network = {}
    with open('test.txt' if not args.test else 'sample.txt') as f:
        for path in f.readlines():
            src, dest = path.strip().split('-')

            if src != 'end' and dest != 'start':
                network.setdefault(src, []).append(dest)

            if dest != 'end' and src != 'start':
                network.setdefault(dest, []).append(src)

    """
        network -> {
            'start': ['A', 'b'],
            'A': ['c', 'b', 'end'],
            'c': ['A'],
            'b': ['A', 'd', 'end'],
            'd': ['b']
        }
    """
    print(network)

    seen = {}
    count = [0, 36]
    walk(network, seen, 'start', count)

    if args.test:
        assert count[0] == 10
        assert count[1] == 36
    else:
        assert count[0] == 4549
        print(f'Part 1: {count[0]}')
        # print(f'Part 2: {}')
