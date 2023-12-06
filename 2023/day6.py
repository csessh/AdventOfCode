from typing import List, Tuple


def count_possible_wins(race: List[Tuple[int, int]]):
    time, record = race
    count = 0

    for i in range(1, time):
        travelled = i * (time - i)
        if travelled > record:
            count += 1

    return count


if __name__ == '__main__':
    with open('input/day6', 'r') as f:
        times = list(map(int, f.readline().split()[1:]))
        distances = list(map(int, f.readline().split()[1:]))

    # Part 1
    result = 1
    races = list(zip(times, distances))
    for race in races:
        result *= count_possible_wins(race)

    print(result)

    # Part 2
    race = (62649190, 553101014731074)
    count = count_possible_wins(race)

    print(count)