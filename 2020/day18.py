from typing import List


def calculate(prob: str, order: List[str]):
    if "(" in prob:
        openp = 0
        start = prob.index("(")
        for i in range(start, len(prob)):
            if prob[i] == "(":
                openp += 1
            elif prob[i] == ")":
                openp -= 1
            if openp == 0:
                break

        return calculate(
            prob[:start] + calculate(prob[start + 1 : i], order) + prob[i + 1 :],
            order
        )
    else:
        grams = prob.split(" ")
        for ops in order:
            i = 1
            while i < len(grams):
                if grams[i] in ops:
                    grams = (
                        grams[: i - 1]
                        + [str(eval(" ".join(grams[i - 1 : i + 2])))]
                        + grams[i + 2 :]
                    )

                else:
                    i += 2
        return grams[0]


if __name__ == '__main__':
    with open('test.txt') as f:
        problems = f.readlines()

    part1 = sum([int(calculate(problem, ["+*"])) for problem in problems])
    print(f"Part 1: {part1}")

    part2 = sum([int(calculate(problem, ["+", "*"])) for problem in problems])
    print(f"Part 2: {part2}")