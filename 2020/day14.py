#!/Users/thangdo/Documents/dev/csessh/bin/python


from os import stat
from typing import Dict, List, Tuple


MEMORY_SIZE = 36
memory = {}


class Mask:
    def __init__(self, mask: str):
        self._raw = mask[len('mask = '):]
        self._bit_masks = {}

        for idx, c in enumerate(self._raw):
            if c != 'X':
                self._bit_masks[MEMORY_SIZE - (idx + 1)] = int(c)

    def __repr__(self) -> str:
        return self._raw

    @property
    def bits(self) -> Dict[int, int]:
        return self._bit_masks

    @staticmethod
    def set_bit(value: int, loc: int, bit: int) -> int:
        """
        For example:
            value = 0 --> 0000

            set_bit(0, 1) flips the rightmost bit to 1
                --> value = 1 --> 0001
        """
        if bit == 1:
            return value | (1 << loc)

        if bit == 0:
            return value &~ (1 << loc)


def get_sum_of_values_in_memory(instructions: Dict[str, List[Tuple[int, int]]]) -> int:
    """
    What is the sum of all values left in memory after it completes?
    """
    for mask, instruction in instructions.items():
        for index, value in instruction:
            pre_mask = value
            masked_value = pre_mask
            for loc, bit in mask.bits.items():
                masked_value = Mask.set_bit(masked_value, loc, bit)

            memory[index] = masked_value
    return sum(memory.values())


if __name__ == '__main__':
    instructions = {}

    with open('test.txt', 'r') as f:
        current_mask = None
        for line in f.readlines():
            line = line.strip()

            if line.startswith('mask'):
                mask = Mask(line)
                instructions[mask] = []
                current_mask = mask
            else:
                index = line[len('mem['): line.index(']')]
                value = int(line[line.index('=')+1:])
                instructions[current_mask].append((index, value))

    # Part 1
    print(f'Part 1: {get_sum_of_values_in_memory(instructions)}')
