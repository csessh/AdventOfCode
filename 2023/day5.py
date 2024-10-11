from typing import List


s2s: List[List[int]] = []
s2f: List[List[int]] = []
f2w: List[List[int]] = []
w2l: List[List[int]] = []
l2t: List[List[int]] = []
t2h: List[List[int]] = []
h2l: List[List[int]] = []


def read(blob: str):
    global s2s, s2f, f2w, w2l, l2t, t2h, h2l
    ridiculous_map = None

    for line in blob:
        if line == "\n":
            continue

        if line.strip() == "seed-to-soil map:":
            ridiculous_map = s2s
            continue

        if line.strip() == "soil-to-fertilizer map:":
            ridiculous_map = s2f
            continue

        if line.strip() == "fertilizer-to-water map:":
            ridiculous_map = f2w
            continue

        if line.strip() == "water-to-light map:":
            ridiculous_map = w2l
            continue

        if line.strip() == "light-to-temperature map:":
            ridiculous_map = l2t
            continue

        if line.strip() == "temperature-to-humidity map:":
            ridiculous_map = t2h
            continue

        if line.strip() == "humidity-to-location map:":
            ridiculous_map = h2l
            continue

        ridiculous_map.append(list(map(int, line.split())))


def translate(number: int, func: List[List[int]]) -> int:
    for dest, src, span in func:
        if number >= src and number - src <= span:
            return number - src + dest
    return number


def from_seed_to_location(seed) -> int:
    soil = translate(seed, s2s)
    fertilizer = translate(soil, s2f)
    water = translate(fertilizer, f2w)
    light = translate(water, w2l)
    temp = translate(light, l2t)
    humidity = translate(temp, t2h)
    location = translate(humidity, h2l)

    return location


# def expand(seeds: List[int]) -> List[int]:
#     pairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]


if __name__ == "__main__":
    with open("input/day5", "r") as f:
        data = f.readlines()

    seeds = list(map(int, data[0].split(":")[1].split()))
    read(data[1:])

    lowest_location = None
    for seed in seeds:
        location = from_seed_to_location(seed)

        if not lowest_location or location < lowest_location:
            lowest_location = location

    print(lowest_location)

