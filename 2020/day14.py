from itertools import product
from typing import Dict, List, Tuple


MEMORY_SIZE = 36


class Mask:
    def __init__(self, mask: str):
        self._raw = mask[len('mask = '):]
        self._bit_masks = {}
        self._floating_masks = []

        for idx, c in enumerate(self._raw):
            if c != 'X':
                self._bit_masks[MEMORY_SIZE - (idx + 1)] = int(c)
            else:
                self._floating_masks.append(MEMORY_SIZE - (idx + 1))

    def __repr__(self) -> str:
        return self._raw

    @property
    def bits(self) -> Dict[int, int]:
        return self._bit_masks

    @property
    def floaters(self) -> List[int]:
        return self._floating_masks

    @staticmethod
    def mask_value(value: int, loc: int, bit: int) -> int:
        """
        For example:
            mask_value(0, 1, 1) flips the rightmost bit to 1
                --> old = 0 --> 0000
                --> value = 1 --> 0001

            mask_value(1, 1, 0) flips the rightmost bit to 0
                --> old = 1 --> 0001
                --> value = 0 --> 0000
        """
        if bit == 1:
            return value | (1 << loc)

        if bit == 0:
            return value &~ (1 << loc)


def get_sum_of_values_in_memory_1(instructions: Dict[str, List[Tuple[int, int]]]) -> int:
    memory = {}
    for mask, instruction in instructions.items():
        for index, value in instruction:
            for loc, bit in mask.bits.items():
                value = Mask.mask_value(value, loc, bit)
            memory[index] = value
    return sum(memory.values())


def get_sum_of_values_in_memory_2(instructions: Dict[str, List[Tuple[int, int]]]) -> int:
    memory = {}
    for mask, instruction in instructions.items():
        for address, value in instruction:
            overflown_addresses = []

            for loc, bit in mask.bits.items():
                if bit == 1:
                    address = Mask.mask_value(address, loc, bit)

            for combo in list(product(range(2), repeat=len(mask.floaters))):
                new_address = address
                for bit_placement in zip(mask.floaters, combo):
                    loc, bit = bit_placement
                    new_address = Mask.mask_value(new_address, loc, bit)
                    overflown_addresses.append(new_address)

            for overflown_address in overflown_addresses:
                memory[overflown_address] = value
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
                index = int(line[len('mem['): line.index(']')])
                value = int(line[line.index('=')+1:])
                instructions[current_mask].append((index, value))

    """
    instruction --> {
        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X: [
            ('8', 11),  # memory location (8) and value to be written (11)
            ('7', 101),
            ('8', 0)
        ]
    }
    """

    # Part 1
    print(f'Part 1: {get_sum_of_values_in_memory_1(instructions)}')

    # Part 2
    print(f'Part 2: {get_sum_of_values_in_memory_2(instructions)}')
