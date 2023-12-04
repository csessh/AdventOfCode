from dataclasses import dataclass
from typing import List
from collections import defaultdict


if __name__ == '__main__':
    with open('input/day4', 'r') as f:
        cards = f.readlines()

    point = 0
    tally = defaultdict(int)

    for card in cards:
        card = card.strip().split(': ')

        id=int(card[0].split()[1])
        tally[id] += 1

        winners=set(map(int, card[1].split(' | ')[0].split()))
        draws=set(map(int, card[1].split(' | ')[1].split()))
        matches=draws.intersection(winners)

        for i in range(id+1, id+len(matches)+1):
            if i > len(cards):
                break
            tally[i] += tally[id]

        if matches:
            point += 2**(len(matches)-1)

    # Part 1
    print(point)

    # Part 2
    print(sum(tally.values()))
