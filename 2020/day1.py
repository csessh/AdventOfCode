#!/Users/thangdo/Documents/dev/csessh/bin/python

def read():
    with open('test.txt') as f:
        temp = f.readlines()
        data = set(list(map(int, temp)))
    return data

def solve_part1(numbers: set, target: int=2020):
    for number in numbers:
        the_other_half = target - number
        if the_other_half in numbers:
            return the_other_half, number
    return None, None

def solve_part2(numbers: set):
    taget = 2020

    for x in numbers:
        the_rest = 2020 - x
        y, z = solve_part1(numbers, the_rest)
        if y and z:
            return(x, y, z)
        return None, None, None

if __name__ == '__main__':
    numbers = read()
    a, b = solve_part1(numbers)
    print(a, b, a*b)

    x, y, z = solve_part2(numbers)
    print(x, y, z, x*y*z)