import argparse
from collections import Counter
from typing import Dict


def extend(polymer: Dict[str, int], counter: Dict[str, int], rules: Dict[str, str], step: int):
    for _ in range(step):
        new = []
        for pair, count in polymer.items():
            if count == 0:
                continue

            inserted_char = rules[pair]
            counter[inserted_char] += count

            polymer[pair] -= count

            new_1 = ''.join([pair[0], inserted_char])
            new_2 = ''.join([inserted_char, pair[1]])
            new.append((new_1, count))
            new.append((new_2, count))

        for n, count in new:
            polymer[n] += count


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        template = f.readline().strip()
        counter = Counter(template)
        template = [''.join(p) for p in list(zip(template, template[1:]))]

        f.readline()

        rules = {
            pair: char for pair, char in [line.strip().split(' -> ') for line in f.readlines()]
        }

        pairs = {
            pair: 0 for pair in rules.keys()
        }

        for p in template:
            pairs[p] += 1

    step = 40
    extend(pairs, counter, rules, step)
    _, most = counter.most_common()[0]
    _, least = counter.most_common()[-1]

    if args.test:
        if step == 10:
            assert most - least == 1588
        if step == 40:
            assert most - least == 2188189693529

    print(f'Result after {step} steps = {most-least}')
