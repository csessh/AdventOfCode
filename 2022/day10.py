class Program:
    def __init__(self):
        self.x = 1
        self.cycle = 0
        self.signal = 0
        self.sprite = self.x

    def addx(self, val: int):
        self.draw()
        self.cycle += 1

        if (self.cycle % 40) - 20 == 0 or self.cycle == 20:
            self.signal += self.cycle * self.x

        self.draw()
        self.cycle += 1

        if (self.cycle % 40) - 20 == 0 or self.cycle == 20:
            self.signal += self.cycle * self.x

        self.x += val
        self.sprite = self.x

    def noop(self):
        self.draw()
        self.cycle += 1

        if (self.cycle % 40) - 20 == 0 or self.cycle == 20:
            self.signal += self.cycle * self.x

    def interpret(self, command: str):
        command = command.strip()

        if command.startswith("addx "):
            self.addx(int(command[5:]))
        else:
            self.noop()

    def draw(self):
        if self.cycle % 40 == 0:
            print()

        if self.sprite - 1 <= self.cycle % 40 <= self.sprite + 1:
            print("@", end="")
        else:
            print(".", end="")


if __name__ == "__main__":
    with open("input/day10") as f:
        commands = f.readlines()

    program = Program()

    for command in commands:
        program.interpret(command.strip())

    print(f"\n\nPart 1: Signal strength is {program.signal}")
