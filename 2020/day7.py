import re

rules = {}


with open('test.txt', 'r') as f:
    ridiculous_rules = f.readlines()


def can_this_bag_hold_shiny_stuff(bag: str) -> bool:
    if rules[bag] is None:
        return False

    if 'shiny gold' in rules[bag].keys():
        return True
    else:
        for sub in rules[bag].keys():
            if can_this_bag_hold_shiny_stuff(sub):
                return True
        return False


def how_many_bags_can_one_bag_carries(rule: str):
    global rules
    bag, inside = rule.split('bags contain')

    if 'no other bags' in inside:
        rules[bag.strip()] = None
    else:
        content = {}
        for sub_bag in inside.split(','):
            quantity = re.match(r'^([0-9]+) (\w+ \w+).+$', sub_bag.strip()).group(1).strip()
            bag_type = re.match(r'^([0-9]+) (\w+ \w+).+$', sub_bag.strip()).group(2).strip()

            if bag_type in content:
                raise ValueError

            content[bag_type] = int(quantity)
        rules[bag] = content


def how_many_bags_can_fit_within_this_bag(root: dict, multiplier: int) -> int:
    if root == None:
        return 0

    total = sum(root.values()) * multiplier
    for bag, count in root.items():
        total += how_many_bags_can_fit_within_this_bag(rules[bag], count*multiplier)
    return total


def solve_part1():
    count = 0
    for bag in rules.keys():
        if can_this_bag_hold_shiny_stuff(bag):
            count += 1
    print(count)


def solve_part2():
    shiny_gold = rules['shiny gold']
    print(how_many_bags_can_fit_within_this_bag(shiny_gold, 1))


if __name__ == '__main__':
    for rule in ridiculous_rules:
        how_many_bags_can_one_bag_carries(rule)

    solve_part1()
    solve_part2()
