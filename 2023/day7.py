from typing import List
from collections import Counter
from enum import Enum, auto


class Card:
    def __init__(self, face: str):
        self.face = face

        try:
            self.value = int(face)
        except ValueError:
            if face == 'T':
                self.value = 10
            elif face == 'J':
                self.value = 1  # Part 1: Value = 11 | Part 2: Value = 1
            elif face == 'Q':
                self.value = 12
            elif face == 'K':
                self.value = 13
            elif face == 'A':
                self.value = 14

    def __str__(self) -> str:
        return self.face

    def __repr__(self) -> str:
        return self.face


class Hand:
    def __init__(self, cards: List[str], bid: int):
        self.hand = list(map(Card, cards))
        self.bid = bid
        self._set = Counter(cards)

        _map = {
            '[1, 1, 1, 1, 1]': 0,
            '[1, 1, 1, 2]': 1,
            '[1, 2, 2]': 2,
            '[1, 1, 3]': 3,
            '[2, 3]': 4,
            '[1, 4]': 5,
            '[5]': 6
        }

        """
        Part 2 with Jokers
        """
        jokers_count = self._set.pop('J', 0)
        if jokers_count != 5:
            face, _ = self._set.most_common(1)[0]
            self._set[face] += jokers_count
        else:
            self._set['J'] = jokers_count
        """
        Part 2 with Jokers
        """

        _key = sorted(self._set.values())
        self.value = _map.get(str(_key), 0)

    def __repr__(self) -> str:
        return f'{self.hand} | type {self.value} | bid {self.bid}'

    def __gt__(self, other: 'Hand') -> bool:
        if self.value == other.value:
            for i in range(len(self.hand)):
                if self.hand[i].value > other.hand[i].value:
                    return True

                if self.hand[i].value < other.hand[i].value:
                    return False

        return self.value > other.value


if __name__ == '__main__':
    with open('input/day7', 'r') as f:
        game = f.readlines()

    hands = []
    for hand in game:
        cards, bid = hand.split()
        bid = int(bid)
        hands.append(Hand(cards, bid))

    result = 0
    for idx, hand in enumerate(sorted(hands), start=1):
        result += hand.bid * (idx)
        print(hand, f'| rank {idx} | winning {hand.bid * (idx)}')

    print(result)