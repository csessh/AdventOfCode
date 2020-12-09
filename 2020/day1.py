#!/Users/thangdo/Documents/dev/csessh/bin/python
from typing import Tuple, Union


def find_combo_of_2(numbers: Union[set, list], target: int=2020) -> Tuple[int, int]:
    for number in numbers:
        the_other_half = target - number
        if the_other_half in numbers:
            return the_other_half, number
    return None, None


def find_combo_of_3(numbers: set, target: int=2020) -> Tuple[int, int, int]:
    for x in numbers:
        sub_target = target - x
        y, z = find_combo_of_2(numbers, sub_target)
        if y and z:
            return(x, y, z)
    return None, None, None


if __name__ == '__main__':
    with open('test.txt') as f:
        temp = f.readlines()
        data = set(list(map(int, temp)))

    """
    Part 1: Target is set to 2020, we look for 2 numbers that add up to target
    """
    a, b = find_combo_of_2(data)
    print(a, b, a*b)


    """
    Part 2: Target is set to 2020, we look for 3 numbers that add up to target
    """
    x, y, z = find_combo_of_3(data)
    print(x, y, z, x*y*z)