from collections.abc import Iterator
from itertools import tee
from typing import Union, Tuple, Any


def pairwise(iterable: Union[set, list]) -> Iterator[Tuple[Any, Any]]:
    """
    pairwise([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22])
        ->      [1, 3, 1, 1, 1, 3,  1,  1,  3,  1,  3,  3]
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


with open('test.txt', 'r') as f:
    data = [int(x) for x in f.readlines()]
    data += [0, max(data) + 3]
    data = sorted(data)


if __name__ == '__main__':
    # Part 1
    jolts = [y-x for x,y in pairwise(data)]
    print(jolts.count(1) * jolts.count(3))

    # Part 2
    variations = {0: 1}
    for adapter in data[1:]:
        three_jolt_configs = variations.get(adapter-3, 0)
        two_jolt_config = variations.get(adapter-2, 0)
        one_jolt_config = variations.get(adapter-1, 0)
        variations[adapter] = three_jolt_configs + two_jolt_config + one_jolt_config

    print(variations[data[-1]])
