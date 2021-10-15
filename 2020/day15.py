#!/Users/thangdo/Documents/dev/csessh/bin/python

from typing import List


MAX_ITERATION = 30000000
STARTING_NUMBER_TURN = -1


def part1(data: List[int]) -> int:
    spoken = {}
    turn = 1
    last_spoken = None

    while True:
        if turn > MAX_ITERATION:
            break

        if turn <= len(data):
            last_spoken = data[turn-1]
            print(f'Turn {turn} - number spoken is a starting number: {last_spoken}')
            spoken[last_spoken] = [turn]
        else:
            print(f'Turn {turn} - Considering {last_spoken}:', end=' ')
            if last_spoken in spoken:
                if len(spoken[last_spoken]) == 1:
                    last_spoken = 0
                    print(f'It was the first time it had been spoken. Number spoken this turn: {last_spoken}')
                else:
                    pen, last = spoken[last_spoken][-2], spoken[last_spoken][-1]
                    last_spoken = spoken[last_spoken][-1] - spoken[last_spoken][-2]
                    # print(f'It had been spoken previously in turn {pen} and {last}. Number spoken this turn: {last_spoken}')
            else:
                last_spoken = 0
                print(f'It had never been spoken previously. Number spoken this turn: {last_spoken}')

            if last_spoken in spoken:
                spoken[last_spoken].append(turn)
            else:
                spoken[last_spoken] = [turn]
        turn += 1

    return last_spoken

# assert part1([1,3,2]) == 1
# assert part1([2,1,3]) == 10
# assert part1([1,2,3]) == 27
# assert part1([2,3,1]) == 78
# assert part1([3,2,1]) == 438
# assert part1([3,1,2]) == 1836

if __name__ == '__main__':
    with open('test.txt', 'r') as f:
        data = [int(num) for num in f.readline().split(',')]

    # Part 1 and 2
    print(f'Last spoken number at {MAX_ITERATION}th turn was {part1(data)}')
