#!/Users/thangdo/Documents/dev/csessh/bin/python
from copy import deepcopy


with open('test.txt') as f:
    instruction = [int(x) for x in f.readline().rstrip().split(',')]


def produce_output(noun: int, verb: int) -> int:
    wip = deepcopy(instruction)
    wip[1] = noun
    wip[2] = verb

    pointer = 0
    while wip[pointer] != 99:
        opcode = wip[pointer]
        op1 = wip[pointer+1]
        op2 = wip[pointer+2]
        loc = wip[pointer+3]

        if opcode == 1:
            wip[loc] = wip[op1] + wip[op2]
        elif opcode == 2:
            wip[loc] = wip[op1] * wip[op2]

        pointer += 4
        if pointer >= len(wip):
            raise ValueError
    return wip[0]


def retrace(target: int) -> int:
    for noun in range(0, 100):
        for verb in range(0, 100):
            result = produce_output(noun, verb)
            if result == target:
                return (100*noun) + verb


# Part 1:
print(produce_output(noun=12, verb=2))

# Part 2:
print(retrace(target=19690720))