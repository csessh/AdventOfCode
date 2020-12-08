#!/Users/thangdo/Documents/dev/csessh/bin/python


def calculate_fuel(mass: int) -> int:
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0

    fuel += calculate_fuel(fuel)
    return fuel


with open('test.txt', 'r') as f:
    weights = f.readlines()

print(sum([calculate_fuel(int(mass)) for mass in weights]))
