from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from aocd import get_data
from rich import print


class Part1:
    def __init__(self):
        self._wires = {}

    def process(self, instructions: List[str]):
        for cmd in instructions:
            lhs, rhs = cmd.strip().split(" -> ")
            if not self._wires.get(rhs):
                self._wires[rhs] = lhs


def main():
    data = get_data(day=7, year=2015)
    instructions = data.splitlines()

    part1 = Part1()
    breakpoint()
    part1.process(instructions)


if __name__ == "__main__":
    main()
