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


# ('--------------- Test validate_byr ---------------')
assert validate_byr('2002') is True
assert validate_byr('2003') is False
assert validate_byr(None) is False
# ('-------------------------------------------------')


def validate_iyr(value: str) -> bool:
    """
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    """
    try:
        year = int(value)
        return 2010 <= year <= 2020
    except (ValueError, TypeError):
        return False


# ('--------------- Test validate_iyr ---------------')
assert validate_iyr('2010') is True
assert validate_iyr('2020') is True
assert validate_iyr('2009') is False
assert validate_iyr('2021') is False
assert validate_iyr(None) is False
# ('-------------------------------------------------')


def validate_eyr(value: str) -> bool:
    """
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    """
    try:
        year = int(value)
        return 2020 <= year <= 2030
    except (ValueError, TypeError):
        return False


# ('--------------- Test validate_eyr ---------------')
assert validate_eyr('2020') is True
assert validate_eyr('2030') is True
assert validate_eyr('2019') is False
assert validate_eyr('2031') is False
assert validate_eyr(None) is False
# ('-------------------------------------------------')


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


# ('--------------- Test validate_hgt ---------------')
assert validate_hgt('59in') is True
assert validate_hgt('190cm') is True
assert validate_hgt('190in') is False
assert validate_hgt('190') is False
assert validate_hgt(None) is False
assert validate_hgt('abc') is False
# ('-------------------------------------------------')


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


# ('--------------- Test validate_hcl ---------------')
assert validate_hcl('#123abc') is True
assert validate_hcl('#012abf') is True
assert validate_hcl('#123abz') is False
assert validate_hcl('#123ab') is False
assert validate_hcl('#123abcd') is False
assert validate_hcl(None) is False
# ('-------------------------------------------------')


def validate_ecl(value: str) -> bool:
    """
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    """
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


# ('--------------- Test validate_ecl ---------------')
assert validate_ecl('amb') is True
assert validate_ecl('blu') is True
assert validate_ecl('brn') is True
assert validate_ecl('gry') is True
assert validate_ecl('grn') is True
assert validate_ecl('hzl') is True
assert validate_ecl('oth') is True
assert validate_ecl(' ') is False
assert validate_ecl('test') is False
# ('-------------------------------------------------')


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


# ('--------------- Test validate_pid ---------------')
assert validate_pid('000000001') is True
assert validate_pid('123456789') is True
assert validate_pid('00000001') is False
assert validate_pid('0123456789') is False
assert validate_pid(' ') is False
# ('-------------------------------------------------')


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


if __name__ == '__main__':
    process(part1_validity_check)
    process(part2_validity_check)
