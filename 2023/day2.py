from typing import Dict, List


class Game:
    def __init__(self, game: str) -> None:
        self._max_colour_counts = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        game_id, draws = game.strip().split(':')

        _, game_id = game_id.split()
        self._id = int(game_id)

        self._draws = []
        draws = draws.split('; ')
        for draw in draws:
            cubes = {}
            colours = draw.strip().split(', ')
            for colour in colours:
                count, colour = colour.split()
                cubes[colour] = int(count)
                if int(count) > self._max_colour_counts[colour]:
                    self._max_colour_counts[colour] = int(count)

            self._draws.append(cubes)

    @property
    def minimum_cubes_required(self):
        return self._max_colour_counts['red'], self._max_colour_counts['green'], self._max_colour_counts['blue']

    def can_this_bag_contain(self, red: int, green: int, blue: int) -> bool:
        """
        only 12 red cubes, 13 green cubes, and 14 blue cubes?
        """
        print(self._draws)
        for draw in self._draws:
            if draw.get('red', 0) > red or \
                draw.get('green', 0) > green or \
                draw.get('blue', 0) > blue:
                return False
        return True


if __name__ == '__main__':
    with open('input/day2', 'r') as f:
        data = f.readlines()

    total = 0
    power = 0
    for line in data:
        a = Game(line)
        if a.can_this_bag_contain(red=12, green=13, blue=14):
            total += a._id

        r, g, b = a.minimum_cubes_required
        power += r*g*b

    print(total, power)

