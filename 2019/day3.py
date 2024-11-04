#!/Users/thangdo/Documents/dev/csessh/bin/python
from typing import Tuple


with open("test.txt", "r") as f:
    paths = [path.strip().split(",") for path in f.readlines()]


def traverse(steps: list) -> set:
    steps_taken = []
    x = 0
    y = 0

    for step in steps:
        direction = step[0]
        distance = int(step[1:])

        for i in range(0, distance):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1

            steps_taken.append(
                (
                    x,  # location x
                    y,  # location y
                    abs(x) + abs(y),  # distance to center
                )
            )
    return set(steps_taken)


def retrace(steps: list, destination: Tuple[int, int, int]) -> int:
    x = 0
    y = 0

    count = 0
    for step in steps:
        direction = step[0]
        distance = int(step[1:])

        for i in range(0, distance):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1

            count += 1

            if x == destination[0] and y == destination[1]:
                return count


steps_taken_by_A = traverse(paths[0])
steps_taken_by_B = traverse(paths[1])
cross_overs = list(steps_taken_by_A.intersection(steps_taken_by_B))
cross_overs.sort(key=lambda x: x[2], reverse=False)

# Part 1
print(cross_overs[0][2])

# Part 2
minimum_distance = None
for location in cross_overs:
    steps_retraced_by_A = retrace(paths[0], location)
    steps_retraced_by_B = retrace(paths[1], location)

    if (
        minimum_distance is None
        or steps_retraced_by_A + steps_retraced_by_B < minimum_distance
    ):
        minimum_distance = steps_retraced_by_A + steps_retraced_by_B

print(minimum_distance)
