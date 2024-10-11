from dataclasses import dataclass
from math import lcm


@dataclass(frozen=True)
class Node:
    label: str
    L: str
    R: str

    def __repr__(self) -> str:
        return f"{self.label} = ({self.L}, {self.R})"


if __name__ == "__main__":
    with open("input/day8", "r") as f:
        instructions = f.readline().strip()
        nodes = f.readlines()

    network = {}
    starting_points = []
    for node in nodes:
        if node.strip():
            label, neighbours = node.strip().split(" = ")
            L, R = neighbours.strip()[1:-1].split(", ")

            network[label] = Node(label, L, R)

            if label.endswith("A"):
                starting_points.append(network[label])

    # Part 1
    current_node = network["AAA"]
    step = 0
    while True:
        command = instructions[step % len(instructions)]
        current_node = (
            network[current_node.R] if command == "R" else network[current_node.L]
        )
        step += 1
        if current_node.label == "ZZZ":
            break

    print(step)

    # Part 2
    steps = []
    for node in starting_points:
        current_node = node
        step = 0
        while True:
            command = instructions[step % len(instructions)]
            current_node = (
                network[current_node.R] if command == "R" else network[current_node.L]
            )
            step += 1
            if current_node.label.endswith("Z"):
                steps.append(step)
                break

    print(lcm(*steps))
