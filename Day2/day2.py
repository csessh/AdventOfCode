COMMAND_GROUP_SIZE = 4
POS_X_OFFSET = 1
POS_Y_OFFSET = 2
POS_Z_OFFSET = 3

ADDITION = 1
MULTIPLY = 2
HALT = 99


if __name__ == '__main__':
    with open('input.txt') as f:
        commands = [int(x) for x in f.readline().rstrip().split(',')]

    for i in range(0, len(commands), COMMAND_GROUP_SIZE):
        x_index = commands[i+POS_X_OFFSET]
        y_index = commands[i+POS_Y_OFFSET]
        x = commands[x_index]
        y = commands[y_index]

        if commands[i] == ADDITION:
            z = x + y
        elif commands[i] == MULTIPLY:
            z = x * y
        elif commands[i] == HALT:
            break

        z_index = commands[i+POS_Z_OFFSET]
        commands[z_index] = z

    print(commands[0])


