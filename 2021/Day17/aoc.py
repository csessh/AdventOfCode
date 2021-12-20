import argparse
from typing import Tuple


def advance(velocity: Tuple[int, int],
            target_x: Tuple[int, int],
            target_y: Tuple[int, int]) -> Tuple[bool, int]:
    x, y = (0, 0)
    vx, vy = velocity

    peak = y

    lx, hx = target_x
    ly, hy = target_y

    while True:
        x += vx
        y += vy

        if y > peak:
            peak = y

        if lx <= x <= hx and ly <= y <= hy:
            return True, peak

        if x > hx or y < ly:
            return False, peak

        vy -= 1
        if vx < 0:
            vx += 1
        elif vx > 0:
            vx -= 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        x, y = f.readline().strip()[len('target area: '):].split(', ')
        tx = [int(i) for i in x[2:].split('..')]
        ty = [int(i) for i in y[2:].split('..')]

    #
    # Part 1
    #
    max_peak = 0

    #
    # Part 2
    #
    bulleyes = 0

    for vx in range(max(tx)+1):
        for vy in range(min(ty), max(tx)):
            sucess, peak = advance((vx, vy), tx, ty)
            if sucess:
                bulleyes += 1
                if peak > max_peak:
                    max_peak = peak

    if args.test:
        assert advance((9,0), tx, ty)[0] == True
        assert advance((7,2), tx, ty)[0] == True
        assert advance((6,3), tx, ty)[0] == True
        assert advance((6,9), tx, ty) == (True, 45)
        assert advance((17,-4), tx, ty)[0] == False
        assert advance((20,20), tx, ty)[0] == False
        assert max_peak == 45

    print(f'Part 1: {max_peak}')
    print(f'Part 2: {bulleyes}')