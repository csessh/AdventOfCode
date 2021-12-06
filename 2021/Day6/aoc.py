import argparse
from enum import Enum
from typing import List


class InternalTimer(int, Enum):
    Min = 0
    Reset = 6
    New = 8


class Fish:
    def __init__(self, timer: int=InternalTimer.New):
        self._internal_timer = timer

    def age(self):
        if self._internal_timer > InternalTimer.Min:
            self._internal_timer -= 1
        elif self._internal_timer == InternalTimer.Min:
            self._internal_timer = InternalTimer.Reset

    @staticmethod
    def spawn() -> 'Fish':
        return Fish(timer=InternalTimer.New)

    def __repr__(self) -> str:
        return f'Fish {self._internal_timer}'

    @property
    def timer(self) -> int:
        return self._internal_timer


def count_lanternfish(days: int, school: List[Fish]) -> int:
    for _ in range(days):
        newborns = []
        for idx, fish in enumerate(school):
            current_age = fish.timer
            fish.age()

            if fish.timer == InternalTimer.Reset and current_age == InternalTimer.Min:
                newborns.append(Fish.spawn())
        school += newborns

    return len(school)


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    lines = []
    with open('test.txt' if not args.test else 'sample.txt') as f:
        school_of_fish = list(map(Fish, map(int, f.readline().strip().split(','))))

    if args.test:
        assert count_lanternfish(80, school_of_fish) == 5934
        # assert count_lanternfish(256, school_of_fish) == 26984457539

