#!/Users/thangdo/Documents/dev/csessh/bin/python
from typing import Tuple


with open('test.txt', 'r') as f:
    paths = [path.strip().split(',') for path in f.readlines()]


def traverse(steps: list) -> set:
    steps_taken = []
    x = 0
    y = 0

    for step in steps:
        direction = step[0]
        distance = int(step[1:])

        for i in range(0, distance):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1

            steps_taken.append(
                (
                    x,              # location x
                    y,              # location y
                    abs(x) + abs(y) # distance to center
                )
            )
    return set(steps_taken)


def retrace(steps: list, destination: Tuple[int, int]) -> int:
    x = 0
    y = 0

    count = 0
    for step in steps:
        direction = step[0]
        distance = int(step[1:])

        for i in range(0, distance):
            if direction == 'R':
                x += 1
            elif direction == 'L':
                x -= 1
            elif direction == 'U':
                y += 1
            elif direction == 'D':
                y -= 1

            count += 1

            if x == destination[0] and y == destination[1]:
                return count


A_steps = traverse(paths[0])
B_steps = traverse(paths[1])
cross_overs = list(A_steps.intersection(B_steps))
cross_overs.sort(key=lambda x: x[2], reverse=False)

# Part 1
print(cross_overs[0][2])

# Part 2
distance = None
for location in cross_overs:
    A_retrace = retrace(paths[0], location)
    B_retrace = retrace(paths[1], location)

    if distance is None or A_retrace + B_retrace < distance:
        distance = A_retrace + B_retrace

print(distance)
