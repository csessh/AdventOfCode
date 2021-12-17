import argparse
from typing import List, Dict, NamedTuple


def decode_literal(packet: str):
    idx = 6
    literal = ''
    while True:
        group = packet[idx:idx+5]
        literal += group[1:]
        idx += 5

        if int(group[0]) == 0:
            break

    return int(literal, 2)

def decode_operator(packet: str):
    length_signal = int(packet[6])
    print(f'Length signal = {length_signal}')
    if length_signal == 0:
        print(f'Next 15 bits {packet[7:7+15]} = {int(packet[7:7+15], 2)}')
        print(f'{int(packet[7:7+15], 2)} sub-packet(s): {packet[7+15:]}')
        decode(packet[7+15:])
    elif length_signal == 1:
        print(f'Next 11 bits {packet[7:7+11]} = {int(packet[7:7+11], 2)}')
        print(f'{int(packet[7:7+11], 2)} sub-packet(s): {packet[7+11:]}')
        decode(packet[7+11:])


def decode(packet: str) -> int:
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)

    print(f'Decoding: {packet}, V{version}, T{type_id}')

    if type_id == 4:
        decode_literal(packet)
    else:
        decode_operator(packet)

    return version


if __name__ == '__main__':
    parser = argparse.ArgumentParser('AoC')
    parser.add_argument('-t', '--test', help="Run sample input and verify answers", action="store_true")
    args = parser.parse_args()

    with open('test.txt' if not args.test else 'sample.txt') as f:
        lines = [f'{int(line.strip(), 16):04b}' for line in f.readlines()]

    for line in lines:
        decode(line)

    # print(f'Part 1: {version_sums}')
