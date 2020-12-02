def calculate_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel <= 0:
        return 0

    fuel += calculate_fuel(fuel)
    return fuel

if __name__ == '__main__':
    with open('input.txt') as f:
        weights = f.readlines()

    total = sum([calculate_fuel(int(mass)) for mass in weights])
    print(total)
