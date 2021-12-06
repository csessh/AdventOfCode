import argparse
import re
import numpy
from collections import defaultdict
from typing import List, Dict, NamedTuple


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    lines = []
    with open('test.txt' if not args.test else 'sample.txt') as f:
        for data in f.readlines():
            pass


    # assert part 1
    # assert part 2
