
def calculate(s, order):
    if "(" in s:
        openp = 0
        start = s.index("(")
        for i in range(start, len(s)):
            if s[i] == "(":
                openp += 1
            elif s[i] == ")":
                openp -= 1
            if openp == 0:
                break
        return calculate(s[:start] + calculate(s[start + 1 : i], order) + s[i + 1 :], order)

    else:
        grams = s.split(" ")
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


with open('test.txt') as f:
    probs = f.readlines()

part1 = sum([int(calculate(l, ["+*"])) for l in probs])
print(f"Part 1: {part1}")

part2 = sum([int(calculate(l, ["+", "*"])) for l in probs])
print(f"Part 2: {part2}")