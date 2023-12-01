import re


# Part 1 pattern
# PATTERN = r'[0-9]'

# Part 2 pattern
PATTERN = r'(?=([0-9]|one|two|three|four|five|six|seven|eight|nine))'


words_to_numbers = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


def extract(data: str) -> int:
    matches = re.findall(PATTERN, data)
    first = int(matches[0]) if matches[0].isnumeric() else words_to_numbers[matches[0]]
    last = int(matches[-1]) if matches[-1].isnumeric() else words_to_numbers[matches[-1]]
    return first*10 + last


if __name__ == '__main__':
    with open('input/day1', 'r') as f:
        data = f.readlines()

    total = 0
    for line in data:
        calibration_value = extract(line.strip())
        total += calibration_value

    print(total)