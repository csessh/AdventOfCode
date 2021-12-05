SLIDING_WINDOW_OFFSET = 3


if __name__ == '__main__':
    with open('test.txt') as f:
        readings = [int(reading.strip()) for reading in f.readlines()]

    #
    # Part 1: Single measurement
    #
    prev = 0
    count = -1
    for reading in readings:
        if reading > prev:
            count += 1
        prev = reading
    print(f'Part 1: {count}')


    #
    # Part 2: Sliding window of three
    #
    prev = 0
    count = -1
    for idx, _ in enumerate(readings):
        measurement = sum(readings[idx:idx+SLIDING_WINDOW_OFFSET])
        if measurement > prev:
            count += 1
        prev = measurement
    print(f'Part 2: {count}')
