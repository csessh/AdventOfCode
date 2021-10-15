#!/Users/thangdo/Documents/dev/csessh/bin/python

from typing import List

PART_1_MAX_ITERATION = 2020
PART_2_MAX_ITERATION = 30000000


def last_spoken_number(data: List[int]):
    spoken = {}
    turn = 1
    last_spoken = None

    while True:
        if turn > PART_2_MAX_ITERATION:
            break

        if turn <= len(data):
            last_spoken = data[turn-1]
            # print(f'Turn {turn} - number spoken is a starting number: {last_spoken}')
            spoken[last_spoken] = [turn]
        else:
            # print(f'Turn {turn} - Considering {last_spoken}:', end=' ')
            if last_spoken in spoken:
                if len(spoken[last_spoken]) == 1:
                    last_spoken = 0
                    # print(f'It was the first time it had been spoken. Number spoken this turn: {last_spoken}')
                else:
                    pen, last = spoken[last_spoken][-2], spoken[last_spoken][-1]
                    last_spoken = spoken[last_spoken][-1] - spoken[last_spoken][-2]
                    # print(f'It had been spoken previously in turn {pen} and {last}. Number spoken this turn: {last_spoken}')
            else:
                last_spoken = 0
                # print(f'It had never been spoken previously. Number spoken this turn: {last_spoken}')

            if last_spoken in spoken:
                spoken[last_spoken].append(turn)
            else:
                spoken[last_spoken] = [turn]

        if turn in [PART_1_MAX_ITERATION, PART_2_MAX_ITERATION]:
            print(f'Lask spoken number at {turn}th turn was {last_spoken}')

        turn += 1


if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        data = [int(num) for num in f.readline().split(',')]

    last_spoken_number(data)
