def calculate_fuel(fuel):
    return (fuel // 3) - 2

if __name__ == '__main__':
    with open('input.txt') as f:
        fuels = f.readlines()

    total = sum([calculate_fuel(int(x)) for x in fuels])
    print(total)
