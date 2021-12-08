import argparse


SLIDING_WINDOW_OFFSET = 3


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    lines = []
    with open('test.txt' if not args.test else 'sample.txt') as f:
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

    if args.test:
        assert count == 7
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

    if args.test:
        assert count == 5
    print(f'Part 2: {count}')
