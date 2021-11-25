def convert(data: str) -> dict:
    req, pwd = data.split(':')
    freqs, key = req.split(' ')
    mi, ma = freqs.split('-')

    return {
        'key': key.strip(),
        'min': int(mi),
        'max': int(ma),
        'pwd': pwd.strip()
    }


def is_valid(data: dict) -> bool:
    return data.get('min') <= data.get('pwd').count(data.get('key')) <= data.get('max')


def solve_part1():
    """
    Test data:
        5-11 t: glhbttzvzttkdx

    Convert this line to a lookup (of sort) structure
    {
        'key': 't',
        'min': 5,
        'max': 11,
        'pwd': 'glhbttzvzttkdx'
    }
    """
    count = 0

    with open('test.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
        for line in data:
            entry = convert(line)
            if is_valid(entry):
                count += 1
    print(count)


def convert2(data: str) -> dict:
    req, pwd = data.split(':')
    freqs, key = req.split(' ')
    p1, p2 = freqs.split('-')

    return {
        'key': key.strip(),
        'pos1': int(p1) - 1,    # Reset to index 0
        'pos2': int(p2) - 1,    # Reset to index 0
        'pwd': pwd.strip()
    }


def is_valid2(data: dict) -> bool:
    return (data.get('pwd')[data.get('pos1')] == data.get('key')) != (data.get('pwd')[data.get('pos2')] == data.get('key'))


def solve_part2():
    """
    Test data:
        5-11 t: glhbttzvzttkdx

    Convert this line to a lookup (of sort) structure
    {
        'key': 't',
        'pos1': 5,
        'pos2': 11,
        'pwd': 'glhbttzvzttkdx'
    }

    Note: Index 1? Who does that?
    """
    count = 0

    with open('test.txt') as f:
        data = [line.rstrip() for line in f.readlines()]
        for line in data:
            entry = convert2(line)
            if is_valid2(entry):
                count += 1
    print(count)


solve_part1()
solve_part2()
