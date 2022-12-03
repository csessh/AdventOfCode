#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>


const std::string DAY = "input/day3";
const unsigned int LOWERCASE_OFFSET = 96;
const unsigned int UPPERCASE_OFFSET = 38;

//--------------------------------------------------------------------------------
unsigned int getPriority(const char &item) {
    unsigned int value = 0;

    if (int(item) >= int('a') && int(item) <= int('z'))
        value = int(item) - LOWERCASE_OFFSET;
    else if (int(item) >= int('A') && int(item) <= int('Z'))
        value = int(item) - UPPERCASE_OFFSET;

    return value;
}

//--------------------------------------------------------------------------------
template <typename T> T findCommonItems(T &left, T &right) {
    T common_items;
    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    std::set_intersection(
        left.begin(),
        left.end(),
        right.begin(),
        right.end(),
        std::back_inserter(common_items)
    );

    return common_items;
}

//--------------------------------------------------------------------------------
unsigned int part1(const std::vector<std::string> &rucksacks) {
    unsigned int priority = 0;

    for (auto rucksack : rucksacks) {
        auto mid_index = rucksack.length() / 2;
        auto compartment_1 = rucksack.substr(0, mid_index);
        auto compartment_2 = rucksack.substr(mid_index);
        auto common_items = findCommonItems(compartment_1, compartment_2);
        priority += getPriority(common_items[0]);
    }

    return priority;
}

//--------------------------------------------------------------------------------
unsigned int part2(const std::vector<std::string> &rucksacks) {
    unsigned int priority = 0;

    for (int i = 0; i < rucksacks.size(); i+=3) {
        auto elf_a = rucksacks[i];
        auto elf_b = rucksacks[i+1];
        auto elf_c = rucksacks[i+2];

        auto intersection_a_b = findCommonItems(elf_a, elf_b);
        auto intersection_a_c = findCommonItems(elf_a, elf_c);
        auto common_items = findCommonItems(intersection_a_b, intersection_a_c);

        if (common_items.size() > 0)
            priority += getPriority(common_items[0]);
    }

    return priority;
}

//--------------------------------------------------------------------------------
int main() {
    std::vector<std::string> rucksacks;

    std::ifstream file(DAY);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            rucksacks.push_back(line);
        }
        file.close();
    }

    std::cout << "Part 1: " << part1(rucksacks) << std::endl;
    std::cout << "Part 2: " << part2(rucksacks) << std::endl;

    return 0;
}