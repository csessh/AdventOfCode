from itertools import groupby


with open('test.txt', 'r') as f:
    start, end = f.readline().split('-')


def validate(pwd: int) -> bool:
    if pwd < int(start) or pwd > int(end):
        return False

    decreased = False
    duplicate = False
    prev = 0
    for digit in str(pwd):
        if int(digit) > prev:
            prev = int(digit)
        elif int(digit) == prev:
            duplicate = True
        else:
            return False
    return True and duplicate


valid_pwds = []
for x in range(int(start), int(end)):
    if validate(x):
        valid_pwds.append(str(x))


# Part 1
print(len(valid_pwds))


# Part 2
truly_valid_pwds = []
for pwd in valid_pwds:
    breakdown = [len(''.join(g)) for _, g in groupby(pwd)]
    if 2 in breakdown:
        truly_valid_pwds.append(pwd)


print(len(truly_valid_pwds))
