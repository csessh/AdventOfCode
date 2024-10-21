import re
from abc import ABC, abstractmethod
from typing import List

from aocd import get_data
from rich import print


class Grid(ABC):
    def __init__(self):
        self.on = {}
        self.brightness = 0

    @abstractmethod
    def _toggle(self, start: List[int], end: List[int]):
        pass

    @abstractmethod
    def _turn_on(self, start: List[int], end: List[int]):
        pass

    @abstractmethod
    def _turn_off(self, start: List[int], end: List[int]):
        pass

    def process(self, instructions: List[str]):
        regex = re.compile(r"(\d+,\d+)")
        for line in instructions:
            groups = regex.findall(line)
            start = list(map(int, groups[0].split(",")))
            end = list(map(int, groups[1].split(",")))

            if "toggle" in line:
                self._toggle(start, end)
            elif "turn on" in line:
                self._turn_on(start, end)
            elif "turn off":
                self._turn_off(start, end)


class Part1(Grid):
    def _toggle(self, start: List[int], end: List[int]):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if self.on.get((i, j)):
                    self.on.pop((i, j), None)
                else:
                    self.on[(i, j)] = True

    def _turn_on(self, start: List[int], end: List[int]):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.on[(i, j)] = True

    def _turn_off(self, start: List[int], end: List[int]):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.on.pop((i, j), None)


class Part2(Grid):
    def _toggle(self, start: List[int], end: List[int]):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.on[(i, j)] = self.on.get((i, j), 0) + 2
                self.brightness += 2

    def _turn_on(self, start: List[int], end: List[int]):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.on[(i, j)] = self.on.get((i, j), 0) + 1
                self.brightness += 1

    def _turn_off(self, start: List[int], end: List[int]):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if self.on.get((i, j), 0):
                    self.on[(i, j)] -= 1
                    self.brightness -= 1


def main():
    data = get_data(day=6, year=2015)
    lines = data.splitlines()

    part1 = Part1()
    part1.process(lines)
    print(f"Part1 = {len(part1.on)}")

    part2 = Part2()
    part2.process(lines)
    print(f"Part2 = {part2.brightness}")


if __name__ == "__main__":
    main()
