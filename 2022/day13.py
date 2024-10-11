from typing import List, Union
from functools import cmp_to_key


def sanitize(line: str) -> List:
    if "os." in line:
        raise ValueError
    return eval(line)


def are_they_in_correct_order(
    left: Union[List, int], right: Union[List, int], level: int = 0
) -> int:
    print(f'{"  "*level}- Compare {left} vs {right}')

    if type(left) is int and type(right) is list:
        left = [left]
        print(f'{"  "*level}- Mixed types; convert left to {left} and retry comparison')
    elif type(right) is int and type(left) is list:
        right = [right]
        print(
            f'{"  "*level}- Mixed types; convert right to {right} and retry comparison'
        )

    if type(right) is list and type(left) is list:
        idx = 0
        result = 0
        while True:
            if len(left) == len(right) and idx == len(left):
                return 0

            if idx >= len(left):
                return 1

            if idx >= len(right):
                return -1

            result = are_they_in_correct_order(left[idx], right[idx], level + 1)

            if result == 0:
                idx += 1
                continue

            return result

    elif type(right) is int and type(left) is int:
        if left < right:
            return 1
        elif left == right:
            return 0
        else:
            return -1


if __name__ == "__main__":
    with open("input/day13") as f:
        data = [line.strip() for line in f.readlines()] + [""]

    pair_index = 0
    left = None
    right = None
    result = 0

    for idx, line in enumerate(data):
        print(line)
        if (idx + 1) % 3 == 1:
            left = sanitize(line)
        elif (idx + 1) % 3 == 2:
            right = sanitize(line)
        elif (idx + 1) % 3 == 0:
            pair_index += 1

            print(f"== Pair {pair_index} ==")
            if are_they_in_correct_order(left, right) == 1:
                result += pair_index
                print(f"== Pair {pair_index} - Correct ==")
            else:
                print(f"== Pair {pair_index} - Incorrect ==")
            print()

    print(f"Part 1: Sum of correct pairs indices = {result}")

    data = [sanitize(line) for line in data + ["[[2]]", "[[6]]"] if line != ""]
    data = sorted(data, key=cmp_to_key(are_they_in_correct_order), reverse=True)
    signal = 1

    for idx, line in enumerate(data):
        print(idx, line)

        if line in [[[2]], [[6]]]:
            signal *= idx + 1

    print(f"Part 2: decoder key for distress signal = {signal}")
