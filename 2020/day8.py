#!/Users/thangdo/Documents/dev/csessh/bin/python
from copy import deepcopy


with open('test.txt', 'r') as f:
    BROKEN_CODE = [command.split(' ') + [False] for command in f.readlines()]


class Command:
    ptr = 0
    accumulator = 0
    instruction = None

    def __init__(self, cmd: list):
        self._cmd = cmd[0]
        self._value = int(cmd[1])

    def execute(self):
        if Command.instruction[Command.ptr][2] is True:
            raise ValueError(Command.accumulator)

        Command.instruction[Command.ptr][2] = True
        if self._cmd == 'nop':
            Command.ptr += 1
        elif self._cmd == 'acc':
            Command.ptr += 1
            Command.accumulator += self._value
        elif self._cmd == 'jmp':
            Command.ptr += self._value

    @property
    def next(self):
        try:
            next_cmd = Command.instruction[Command.ptr]
            return Command(next_cmd)
        except IndexError:
            return None


def run(instruction: list) -> int:
    Command.instruction = instruction
    node = Command(Command.instruction[0])
    while node.next:
        node.execute()
        if node.next:
            node = node.next
        else:
            break
    return node.accumulator


# Part 1:
print('=====Part 1============')
try:
    attempt = deepcopy(BROKEN_CODE)
    print(f'Execution result: {run(attempt)}')
except ValueError as e:
    print(f'ValueError: {str(e)}')


# Part 2
print('=====Part 2============')
for i in range(len(BROKEN_CODE)):
    attempt = deepcopy(BROKEN_CODE)
    Command.ptr = 0
    Command.accumulator = 0

    if attempt[i][0] == 'nop':
        attempt[i][0] = 'jmp'
    elif attempt[i][0] == 'jmp':
        attempt[i][0] = 'nop'
    else:
        continue

    try:
        print(f'Execution result: {run(attempt)}')
        break
    except ValueError:
        continue
