import argparse
from typing import List, Dict, NamedTuple


vsum = 0


def decode_4(data: str):
    size = 0
    literal = ''

    while True:
        group = data[size:size+5]
        literal += group[1:]
        size += 5

        if int(group[0]) == 0:
            return size


def decode_0(data: str):
    cbit = int(data[:15], 2)

    n = 0
    while n < cbit:
        n += decode(data[15+n: 15+cbit])

    return 15 + cbit


def decode_1(data: str):
    subs = int(data[:11], 2)

    size = 11
    n = 0
    for _ in range(subs):
        n += decode(data[size+n:])

    size += n
    return size


def decode(packet: str):
    global vsum

    vsum += int(packet[:3], 2)
    type = int(packet[3:6], 2)

    size = 6
    if type == 4:
        print(f'V{int(packet[:3], 2)} T{type} - Literal')

        size += decode_4(packet[6:])
    else:
        print(f'V{int(packet[:3], 2)} T{type} - ', end='')

        if type == 0:
            print('Sum')
        elif type == 1:
            print('product')
        elif type == 2:
            print('minimum')
        elif type == 3:
            print('maximum')
        elif type == 5:
            print('greater')
        elif type == 6:
            print('less')
        elif type == 7:
            print('equal')


        if int(packet[6]) == 0:
            size += decode_0(packet[7:]) + 1
        elif int(packet[6]) == 1:
            size += decode_1(packet[7:]) + 1
    return size


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        lines = [f'{int(line.strip(), 16):4b}' for line in f.readlines()]

    for line in lines:
        if len(line) % 4 != 0:
            line = '0'*(4 - len(line) % 4) + line

        """
            111 011 1 00000000011 010-100-00001 100-100-00010 001-100-00011 [00000]
            V7  T3  1   3 subs    V2  T4  1     V4  T4  2     V1  T4  3
            V = 7 + 2 + 4 + 1 = 14

            001 110 0 000000000011011 110-100-01010 010-100-10001-00100 [0000000]
            V1  T7  0   27 bits       V6  T4   10   V2  T4       20

            110-100-10111-11110-00101 [000]
            V6  T4        2021

            100 010 1 00000000001 001 010 1 00000000001 101 010 0 000000000001011 110-100-01111 [000]
            V4  T2  1   1 sub     V1  T2  1    1 sub    V5  T2  0     11 bits     V6  T4    15

            011 000 1 00000000010 000 000 0 000000000010110 0001000101010110001011 001 000 1 00000000010 000-100-01100 011-100-01101 [00]
            V3  T0  1   2 subs    V0  T0  0      22 bits
        """
        result = decode(line)

    # assert vsum == 12

    print(f'Part 1: {vsum}')
    print(f'Part 2: {result}')
