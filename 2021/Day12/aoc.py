import argparse
from typing import List, Dict, NamedTuple, Set


all_paths = set()


def walk(network: Dict[str, List[str]], seen: Dict[str, bool], cave: str, count: List[int], path: List[str]):
    if cave.islower():
        seen[cave] = True

    path.append(cave)

    if cave == 'end':
        count[0] += 1
        print(' -> '.join(path))
    else:
        for neighbour in network.get(cave, []):
            if not seen.get(neighbour):
                walk(network, seen, neighbour, count, path)

    path.pop()
    seen[cave] = False


def delve(network: Dict[str, List[str]], small_caves: Dict[str, int], seen: Dict[str, bool], cave: str, special: str, path: List[str]):
    if cave.islower():
        seen[cave] = True
        if cave == special:
            small_caves[cave] += 1

    path.append(cave)

    if cave == 'end':
        global all_paths
        all_paths.add(tuple(path))

        print(special, ' -> '.join(path))
    else:
        for neighbour in network.get(cave, []):
            if not seen.get(neighbour) or (neighbour == special and small_caves.get(neighbour) < 2):
                delve(network, small_caves, seen, neighbour, special, path)

    path.pop()
    seen[cave] = False
    if cave.islower() and cave == special:
        small_caves[cave] -= 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    network = {}
    small_caves = {}

    """
        network -> {
            'start': ['A', 'b'],
            'A': ['c', 'b', 'end'],
            'c': ['A'],
            'b': ['A', 'd', 'end'],
            'd': ['b']
        }
    """
    with open('test.txt' if not args.test else 'sample.txt') as f:
        for path in f.readlines():
            src, dest = path.strip().split('-')

            if src != 'end' and dest != 'start':
                network.setdefault(src, []).append(dest)

            if dest != 'end' and src != 'start':
                network.setdefault(dest, []).append(src)

            if src.islower() and src not in ['start', 'end'] and src not in small_caves:
                small_caves[src] = 0

            if dest.islower() and dest not in ['start', 'end'] and dest not in small_caves:
                small_caves[dest] = 0

    count = [0]

    #
    # Part 1
    #
    path = []
    seen = {}
    walk(network, seen, 'start', count, path)

    #
    # Part 2
    #
    path = []
    seen = {}
    for cave in small_caves.keys():
        delve(network, small_caves, seen, 'start', cave, count, path)

    if args.test:
        assert count[0] == 10
        assert len(all_paths) == 36
    else:
        print(f'Part 1: {count[0]}')
        print(f'Part 2: {len(all_paths)}')
