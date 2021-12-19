import argparse
from typing import List, Dict, NamedTuple


vsum = 0


def decode(packet: str, idx):
    global vsum

    vsum += int(packet[idx:idx+3], 2)
    type = int(packet[idx+3:idx+6], 2)

    idx += 6
    if type == 4:
        literal = ''

        while True:
            group = packet[idx:idx+5]
            literal += group[1:]
            idx += 5

            if int(group[0]) == 0:
                # print(int(literal, 2))
                break
    else:
        if int(packet[idx]) == 0:
            idx += 1
            bit_count = int(packet[idx:idx+15], 2)
            end_idx = idx + 15 + bit_count
            idx += 15

            while idx < end_idx:
                idx = decode(packet, idx)
        elif int(packet[idx]) == 1:
            idx += 1
            sub_count = int(packet[idx:idx+11], 2)
            idx += 11

            for _ in range(sub_count):
                idx = decode(packet, idx)
    return idx


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
        result = decode(line, 0)

    if args.test:
        assert vsum == 31

    print(f'Part 1: {vsum}')
    print(f'Part 2: {result}')
