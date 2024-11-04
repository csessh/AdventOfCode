import re
from abc import ABC, abstractmethod
from typing import List

from aocd import get_data
from rich import print


class Parser(ABC):
    @abstractmethod
    def process(self):
        pass


class Part1(ABC):
    def process(self):
        pass


class Part2(ABC):
    def process(self):
        pass


def main():
    data = get_data(day=1, year=2015)


if __name__ == "__main__":
    main()
