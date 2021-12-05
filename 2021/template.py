import argparse
import numpy
from typing import List, Dict, Tuple, NamedTuple



if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    input_file = 'test.txt' if not args.test else 'sample.txt'
    with open(input_file) as f:
        data = f.readlines()

    # assert part1 == ?
    # assert part2 == ?