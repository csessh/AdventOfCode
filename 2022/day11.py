import re
import os
import time
from typing import Dict


class Monkey:
    pack: Dict[int, 'Monkey'] = {}

    def __init__(self, id: int):
        self.workload = 0
        self._current_item = 0
        self.id = id
        self.items = []
        self.op = None
        self.test = 0
        self.test_positive_target = 0
        self.test_negative_target = 0

    def inspect(self):
        while self.items:
            self.workload += 1

            self._current_item = self.items.pop(0)
            self._current_item = self.recalibrate()
            self._current_item = self._current_item // 3

            if self._current_item % self.test == 0:
                self.throw(self._current_item, self.test_positive_target)
            else:
                self.throw(self._current_item, self.test_negative_target)

    def throw(self, item: int, target: int):
        Monkey.pack[target].items.append(item)

    def __repr__(self) -> str:
        return f'Monkey #{self.id} ({self.workload:3}) - Items {self.items}'

    def recalibrate(self) -> int:
        try:
            var1 = int(self.op[0])
        except ValueError:
            var1 = self._current_item

        try:
            var2 = int(self.op[2])
        except ValueError:
            var2 = self._current_item

        if self.op[1] == '*':
            return var1 * var2
        elif self.op[1] == '-':
            return var1 - var2
        elif self.op[1]  == '+':
            return var1 + var2
        elif self.op[1]  == '/':
            return var1 / var2


if __name__ == '__main__':
    current: Monkey = None

    with open('input/day11') as f:
        for line in f.readlines():
            if match := re.search(r'^Monkey ([0-9]+):$', line):
                current = Monkey(int(match[1]))
                Monkey.pack[current.id] = current

            elif match := re.search(r'^\s*Starting items: ([0-9, ]+)$', line):
                current.items += [int(i.strip()) for i in match[1].split(',')]

            elif match := re.search(r'^\s*Operation: new = (old|[0-9]+) ([\*\+-]) (old|[0-9]+)$', line):
                current.op = (match[1], match[2], match[3])

            elif match := re.search(r'^\s*Test: divisible by ([0-9]+)$', line):
                current.test = int(match[1])

            elif match := re.search(r'^\s*If true: throw to monkey ([0-9]+)$', line):
                current.test_positive_target = int(match[1])

            elif match := re.search(r'^\s*If false: throw to monkey ([0-9]+)$', line):
                current.test_negative_target = int(match[1])

    round = 0
    while round < 20:
        os.system('clear')
        round += 1
        print(f'Starting round #{round}')
        for _, v in Monkey.pack.items():
            v.inspect()

        for _, monkey in Monkey.pack.items():
            print(monkey)

        # time.sleep(1)

    workload = [monkey.workload for _, monkey in Monkey.pack.items()]
    workload.sort()

    print(f'\n\nMonkey business level {workload[-2] * workload[-1]}')

