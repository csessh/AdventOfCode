import re
from collections import defaultdict
from enum import Enum


class ValveStatus(int, Enum):
    Close = 0
    Open = 1


class Valve:
    def __init__(self, raw: str):
        self.name = "Unknown"
        self.rate = 0
        self.others = []
        self.status = ValveStatus.Close

        if groups := re.search(
            r"^Valve ([A-Z]{2}) has flow rate=(\d+); (tunnel leads to valve|tunnels lead to valves) (([A-Z]{2},*\s*)+)$",
            raw,
        ):
            self.name = groups[1]
            self.rate = int(groups[2])
            self.others = [valve.strip() for valve in groups[4].split(",")]

    def open(self) -> int:
        self.status = ValveStatus.Open
        return self.rate

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        if len(self.others) > 1:
            return f'Valve {self.name} has flow rate={self.rate}; tunnels lead to valves {", ".join(self.others)}'
        else:
            return f'Valve {self.name} has flow rate={self.rate}; tunnel lead to valve {", ".join(self.others)}'


if __name__ == "__main__":
    valves = defaultdict()
    current = None

    with open("input/day16") as f:
        data = [line.strip() for line in f.readlines()]

    for line in data:
        valve = Valve(line)
        valves[valve.name] = valve
        print(repr(valve))

        if not current:
            current = valve

    print("\n----\n")

    opened_valves = []

    timer = 0
    while timer < 30:
        timer += 1
        print(f"\n== Minute {timer} ==")

        if opened_valves:
            print(
                f'Valves {" and ".join([valve.name for valve in opened_valves])} are open, releasing {sum([valve.rate for valve in opened_valves])} pressure.'
            )
        else:
            print("No valves are open.")

        # if current.rate == 0 or current.status == ValveStatus.Open:
        #     for next_valve in current.others:
        #         next_valve = valves[next_valve]
        #         if next_valve.status == ValveStatus.Close:
        #             print(f'You move to valve {next_valve}.')
        #             current = next_valve
        #             break
        # elif current.status == ValveStatus.Close:
        #     print(f'You open valve {current.name}.')
        #     current.status = ValveStatus.Open
        #     opened_valves.append(current)
