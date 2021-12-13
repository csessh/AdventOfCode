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


def delve(network, seen, cave, count):
    if cave not in seen and cave.islower():
        seen[cave] = 0

    if cave.islower():
        seen[cave] += 1

    if cave == 'end':
        count[1] += 1
    else:
        for neighbour in network.get(cave, []):
            if neighbour not in seen or seen.get(neighbour) < 2:
                delve(network, seen, neighbour, count)

    if cave.islower():
        seen[cave] -= 1


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

    count = [0, 0]

    seen = {}
    walk(network, seen, 'start', count)

    seen = {}
    delve(network, seen, 'start', count)
    print(count[1])
    if args.test:
        assert count[0] == 10
        assert count[1] == 36
    else:
        assert count[0] == 4549
        print(f'Part 1: {count[0]}')
        # print(f'Part 2: {}')
