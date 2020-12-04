#!/Users/thangdo/Documents/dev/csessh/bin/python
import re
from typing import Callable

with open('test.txt', 'r') as f:
    passport_entries = [entry.strip() for entry in f.readlines()]


def part1_validity_check(passport: dict) -> bool:
    return passport.get('byr') and \
        passport.get('iyr') and \
        passport.get('eyr') and \
        passport.get('hgt') and \
        passport.get('hcl') and \
        passport.get('ecl') and \
        passport.get('pid')


def validate_byr(value: str) -> bool:
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    """
    try:
        year = int(value)
        return 1920 <= year <= 2002
    except (ValueError, TypeError):
        return False

# print('--------------- Test validate_byr ---------------')
# print(validate_byr('2002')) # True
# print(validate_byr('2003')) # False
# print(validate_byr(None))   # False
# print('-------------------------------------------------')


def validate_iyr(value: str) -> bool:
    """
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    """
    try:
        year = int(value)
        return 2010 <= year <= 2020
    except (ValueError, TypeError):
        return False

# print('--------------- Test validate_iyr ---------------')
# print(validate_iyr('2010')) # True
# print(validate_iyr('2020')) # True
# print(validate_iyr('2009')) # False
# print(validate_iyr('2021')) # False
# print(validate_iyr(None))   # False
# print('-------------------------------------------------')


def validate_eyr(value: str) -> bool:
    """
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    """
    try:
        year = int(value)
        return 2020 <= year <= 2030
    except (ValueError, TypeError):
        return False

# print('--------------- Test validate_eyr ---------------')
# print(validate_eyr('2020')) # True
# print(validate_eyr('2030')) # True
# print(validate_eyr('2019')) # False
# print(validate_eyr('2031')) # False
# print(validate_eyr(None))   # False
# print('-------------------------------------------------')


def validate_hgt(value: str) -> bool:
    """
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    """
    try:
        digit = int(value[:-2])
    except (ValueError, TypeError):
        return False

    unit = value[-2:]
    if unit == 'cm':
        return 150 <= digit <= 193
    elif unit == 'in':
        return 59 <= digit <= 76
    else:
        return False

# print('--------------- Test validate_hgt ---------------')
# print(validate_hgt('59in'))  # True
# print(validate_hgt('190cm')) # True
# print(validate_hgt('190in')) # False
# print(validate_hgt('190'))   # False
# print(validate_hgt(None))    # False
# print(validate_hgt('abc'))   # False
# print('-------------------------------------------------')


def validate_hcl(value: str) -> bool:
    """
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    """
    try:
        if re.match(r'^#[0-9a-f]{6}$', value):
            return True
    except TypeError:
        return False
    return False

# print('--------------- Test validate_hcl ---------------')
# print(validate_hcl('#123abc'))  # True
# print(validate_hcl('#012abf'))  # True
# print(validate_hcl('#123abz'))  # False
# print(validate_hcl('#123ab'))   # False
# print(validate_hcl('#123abcd')) # False
# print(validate_hcl(None))       # False
# print('-------------------------------------------------')


def validate_ecl(value: str) -> bool:
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

# print('--------------- Test validate_ecl ---------------')
# print(validate_ecl('amb')) # True
# print(validate_ecl('blu')) # True
# print(validate_ecl('brn')) # True
# print(validate_ecl('gry')) # True
# print(validate_ecl('grn')) # True
# print(validate_ecl('hzl')) # True
# print(validate_ecl('oth')) # True
# print(validate_ecl(' '))   # False
# print(validate_ecl('test')) # False
# print('-------------------------------------------------')


def validate_pid(value: str) -> bool:
    """
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    try:
        if re.match(r'^[0-9]{9}$', value):
            return True
    except TypeError:
        return False
    return False

# print('--------------- Test validate_pid ---------------')
# print(validate_pid('000000001'))    # True
# print(validate_pid('123456789'))    # True
# print(validate_pid('00000001'))     # False
# print(validate_pid('0123456789'))   # False
# print(validate_pid(' '))            # False
# print('-------------------------------------------------')


def part2_validity_check(passport: dict) -> bool:
    return validate_byr(passport.get('byr')) and \
        validate_iyr(passport.get('iyr')) and \
        validate_eyr(passport.get('eyr')) and \
        validate_hgt(passport.get('hgt')) and \
        validate_hcl(passport.get('hcl')) and \
        validate_ecl(passport.get('ecl')) and \
        validate_pid(passport.get('pid'))


def process(validity_check: Callable[[dict], bool]):
    valid_passports = 0
    passport = {}
    for entry in passport_entries + ['']:
        if entry == '':
            # At this point, we're done processing the last passport
            # Is it valid?
            if validity_check(passport):
                valid_passports += 1

            # Reset and move on
            passport = {}
        else:
            fields = entry.split(' ')
            for field in fields:
                key, value = field.split(':')
                passport[key] = value
    print(valid_passports)


process(part1_validity_check)
process(part2_validity_check)
