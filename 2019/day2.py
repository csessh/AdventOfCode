POS_X_OFFSET = 1
POS_Y_OFFSET = 2
POS_Z_OFFSET = 3
DEFAULT_COMMAND_OFFSET = 4

ADDITION = 1
MULTIPLY = 2
HALT = 99

TARGET = 19690720
NOUN = 1
VERB = 2


def get_result(noun, verb):
    return (100 * noun) + verb


def init():
    with open('input.txt') as f:
        return [int(x) for x in f.readline().rstrip().split(',')]


def execute(commands, noun, verb):
    commands[NOUN] = noun
    commands[VERB] = verb

    pointer = 0
    while pointer < len(commands):
        try:
            operation = commands[pointer]

            if operation == HALT:
                operation += 1
                return False

            x_index = commands[pointer+POS_X_OFFSET]
            y_index = commands[pointer+POS_Y_OFFSET]
            z_index = commands[pointer+POS_Z_OFFSET]

            x = commands[x_index]
            y = commands[y_index]
            z = x + y if operation == ADDITION else x * y

            commands[z_index] = z
            pointer += DEFAULT_COMMAND_OFFSET

            if z == TARGET:
                return True
        except IndexError:
            return False

    return False


if __name__ == '__main__':
    for noun in range(0, 100):
        for verb in range(0, 100):
            commands = init()

            if execute(commands, noun, verb):
                print(get_result(noun, verb))



