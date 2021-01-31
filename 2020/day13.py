#!/Users/thangdo/Documents/dev/csessh/bin/python

from typing import Set
from math import ceil


def find_the_earliest_bus(timestamp: int, buses: Set[int]):
    earliest = []
    for busID in buses:
        when = ceil(timestamp / busID) * busID
        if not earliest or when < earliest[1]:
            earliest = (busID, when)
    return earliest


def find_the_earliest_timestamp(buses: Set[int]):
    print(buses)
    return 0


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        stamp = int(f.readline())
        ids = set(int(x) for x in f.readline().strip().split(',') if x != 'x')

    # Part 1
    bus, departure = find_the_earliest_bus(stamp, ids)
    print(bus * (departure - stamp))

    # Part 2
    timestamp = find_the_earliest_timestamp(ids)
    print(timestamp)

