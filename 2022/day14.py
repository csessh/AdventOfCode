from collections import defaultdict
from dataclasses import dataclass


objects = defaultdict()
depth = 0


@dataclass
class Location:
    x: int
    y: int

    def __repr__(self) -> str:
        return f'({self.x} - {self.y})'


def populate(obstacles: str):
    global objects
    global depth

    start = None

    for pos in obstacles:
        x, y = map(int, pos.split(','))

        if y > depth:
            depth = y

        if not start:
            start = Location(x, y)
            objects[(start.x, start.y)] = True
            continue

        end = Location(x, y)
        if start.x == end.x:
            if start.y > end.y:
                for i in range(end.y, start.y+1):
                    objects[(start.x, i)] = True
            else:
                for i in range(start.y, end.y+1):
                    objects[(start.x, i)] = True
        elif start.y == y:
            if start.x > end.x:
                for i in range(end.x, start.x+1):
                    objects[(i, start.y)] = True
            else:
                for i in range(start.x, end.x+1):
                    objects[(i, start.y)] = True

        start = end

    return objects


def drop() -> int:
    global objects
    global depth

    count = 0
    while True:
        location = Location(500, 0)

        settled = False
        while not settled:
            if objects.get((location.x, location.y+1)):
                if objects.get((location.x-1, location.y+1)):
                    if objects.get((location.x+1, location.y+1)):

                        objects[(location.x, location.y)] = True
                        count += 1
                        settled = True
                    else:
                        location.x += 1
                        location.y += 1
                else:
                    location.x -= 1
                    location.y += 1
            else:
                location.y += 1

            if location.y > depth:
                return count


def overflow() -> int:
    global objects
    global depth

    count = 0
    while True:
        location = Location(500, 0)

        settled = False
        while not settled:
            if objects.get((location.x, location.y+1)) or location.y+1 == depth+2:
                if objects.get((location.x-1, location.y+1)) or location.y+1 == depth+2:
                    if objects.get((location.x+1, location.y+1)) or location.y+1 == depth+2:

                        objects[(location.x, location.y)] = True
                        count += 1
                        settled = True
                    else:
                        location.x += 1
                        location.y += 1
                else:
                    location.x -= 1
                    location.y += 1
            else:
                location.y += 1

            if location.y == 0:
                return count


def reset():
    global objects
    objects = defaultdict()


if __name__ == "__main__":
    with open('input/day14') as f:
        data = [line.strip().split(' -> ') for line in f.readlines()]

    for line in data:
        populate(line)
    print(f'Part 1: How many units of sand come to rest before sand starts flowing into the abyss below? {drop()}')

    reset()

    for line in data:
        populate(line)
    print(f'Part 2: How many units of sand come to rest before the source of the sand becomes blocked? {overflow()}')



