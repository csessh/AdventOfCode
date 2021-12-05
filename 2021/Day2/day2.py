if __name__ == '__main__':
    with open('test.txt') as f:
        data = [line.strip().split(' ') for line in f.readlines()]

    # Part 1
    x = y = 0
    for instruction in data:
        direction, val = instruction
        if direction == 'forward':
            x += int(val)

        if direction == 'down':
            y += int(val)

        if direction == 'up':
            y -= int(val)

    print(f'Part 1: {x*y}')

    # Part 2
    x = y = aim = 0
    for instruction in data:
        direction, val = instruction
        if direction == 'forward':
            x += int(val)
            y += aim*int(val)

        if direction == 'down':
            aim += int(val)

        if direction == 'up':
            aim -= int(val)

    print(f'Part 2: {x*y}')