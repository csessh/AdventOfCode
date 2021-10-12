#!/Users/thangdo/Documents/dev/csessh/bin/python


from math import ceil
from typing import Set, Tuple


def find_the_earliest_bus(timestamp: int, buses: Set[Tuple[int, int]]) -> Tuple[int, int]:
    earliest = None
    for _, busID in buses:
        if busID == 'x':
            continue

        when = ceil(timestamp / busID) * busID
        if not earliest or when < earliest[1]:
            earliest = (busID, when)
    return earliest


def find_the_earliest_timestamp(buses: Set[Tuple[int, int]]):
    delta = 1
    timestamp = 0

    for offset, busID in buses:
        while True:
            timestamp += delta

            if (timestamp + offset) % busID == 0:
                delta *= busID
                break
    return timestamp


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        stamp = int(f.readline())
        ids = set((i, int(x)) for i, x in enumerate(f.readline().strip().split(',')) if x != 'x')

    # Part 1
    bus, departure = find_the_earliest_bus(stamp, ids)
    print(f'Part 1: {bus * (departure - stamp)}')

    # Part 2
    timestamp = find_the_earliest_timestamp(ids)
    print(f'Part 2: {timestamp}')

