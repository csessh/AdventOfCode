#!/Users/thangdo/Documents/dev/csessh/bin/python


from typing import Dict, List, Tuple


MEMORY_SIZE = 36


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
            set_bit(0, 1, 1) flips the rightmost bit to 1
                --> old = 0 --> 0000
                --> value = 1 --> 0001

            set_bit(1, 1, 0) flips the rightmost bit to 0
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
                value = Mask.set_bit(value, loc, bit)
            memory[index] = value
    return sum(memory.values())


def get_sum_of_values_in_memory_2(instructions: Dict[str, List[Tuple[int, int]]]) -> int:
    memory = {}

    for mask, instruction in instructions.items():
        for index, value in instruction:
            for loc, bit in mask.bits.items():
                print(mask, index, value, loc, bit)

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
