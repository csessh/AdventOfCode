from abc import ABC, abstractmethod
from collections import Counter

from aocd import get_data
from rich import print

ILLEGAL_STR = ["ab", "cd", "pq", "xy"]
VOWELS = "aeoiu"


class Parser(ABC):
    @abstractmethod
    def process(self, line: str) -> bool:
        pass


class Part1(Parser):
    def _contains_three_vowels(self, line: str) -> bool:
        counter = Counter(list(line))
        count = 0

        for i in VOWELS:
            count += counter.get(i, 0)
            if count >= 3:
                return True

        return False

    def _contains_repeating_letters(self, line: str) -> bool:
        prev = ""
        for i in line:
            if i == prev:
                return True
            prev = i

        return False

    def _contains_illegal_pairs(self, line: str) -> bool:
        for i in ILLEGAL_STR:
            if i in line:
                return True
        return False

    def process(self, line: str) -> bool:
        if self._contains_illegal_pairs(line):
            return False

        if not self._contains_three_vowels(line):
            return False

        if not self._contains_repeating_letters(line):
            return False

        return True


class Part2(Parser):
    def _contain_repeating_pairs(self, line: str) -> bool:
        for i, _ in enumerate(line):
            pair = line[i : i + 2]

            if pair in line[i + 2 :]:
                return True

        return False

    def _contains_repeating_letters(self, line: str) -> bool:
        for i, _ in enumerate(line):
            if i + 2 >= len(line):
                break

            if line[i] == line[i + 2]:
                return True

        return False

    def process(self, line: str) -> bool:
        if not self._contain_repeating_pairs(line):
            return False

        if not self._contains_repeating_letters(line):
            return False

        return True


def main():
    data = get_data(day=5, year=2015)

    total = [0, 0]
    parser1 = Part1()
    parser2 = Part2()

    for line in data.split("\n"):
        if parser1.process(line):
            total[0] += 1

        if parser2.process(line):
            total[1] += 1

    print(f"Part 1 = { total[0] }")
    print(f"Part 2 = { total[1] }")


if __name__ == "__main__":
    main()
