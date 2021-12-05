def p1(active) -> int:
    for _ in range(6):
        new = set()
        xvals = [x[0] for x in active]
        yvals = [y[1] for y in active]
        zvals = [z[2] for z in active]

        for x in range(min(xvals) - 1, max(xvals) + 2):
            for y in range(min(yvals) - 1, max(yvals) + 2):
                for z in range(min(zvals) - 1, max(zvals) + 2):
                    nbrs = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            for dz in [-1, 0, 1]:
                                if dx != 0 or dy != 0 or dz != 0:
                                    if (x + dx, y + dy, z + dz) in active:
                                        nbrs += 1

                    if (x, y, z) not in active and nbrs == 3:
                        new.add((x, y, z))
                    if (x, y, z) in active and nbrs in [2, 3]:
                        new.add((x, y, z))

        active = new

    return len(active)


def p2(active):
    for _ in range(6):
        new = set()
        xvals = [x[0] for x in active]
        yvals = [y[1] for y in active]
        zvals = [z[2] for z in active]
        wvals = [w[3] for w in active]

        for x in range(min(xvals) - 1, max(xvals) + 2):
            for y in range(min(yvals) - 1, max(yvals) + 2):
                for z in range(min(zvals) - 1, max(zvals) + 2):
                    for w in range(min(wvals) - 1, max(wvals) + 2):
                        nbrs = 0
                        for dx in [-1, 0, 1]:
                            for dy in [-1, 0, 1]:
                                for dz in [-1, 0, 1]:
                                    for dw in [-1, 0, 1]:
                                        if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                                            if (x + dx, y + dy, z + dz, w + dw) in active:
                                                nbrs += 1

                        if (x, y, z, w) not in active and nbrs == 3:
                            new.add((x, y, z, w))
                        if (x, y, z, w) in active and nbrs in [2, 3]:
                            new.add((x, y, z, w))

        active = new

    return len(active)



if __name__ == '__main__':
    with open("test.txt") as f:
        data = [line.strip() for line in f.readlines()]

    active = set()
    for y, row in enumerate(data):
        for x, col in enumerate(row):
            if col == '#':
                active.add((y, x, 0))

    print(f'Part 1: {p1(active)}')

    active = set()
    for r, l in enumerate(data):
        for c, p in enumerate(l):
            if p == '#':
                active.add((r, c, 0, 0))

    print(f'Part 2: {p2(active)}')