#include "utils.tpp"
#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

const std::string DAY = "input/day3";
const unsigned int LOWERCASE_OFFSET = 96;
const unsigned int UPPERCASE_OFFSET = 38;

//--------------------------------------------------------------------------------
unsigned int get_priority(const char &item) {
  unsigned int value = 0;

  if (int(item) >= int('a') && int(item) <= int('z'))
    value = int(item) - LOWERCASE_OFFSET;
  else if (int(item) >= int('A') && int(item) <= int('Z'))
    value = int(item) - UPPERCASE_OFFSET;

  return value;
}

//--------------------------------------------------------------------------------
unsigned int part1(const std::vector<std::string> &rucksacks) {
  unsigned int priority = 0;

  for (const auto &rucksack : rucksacks) {
    auto mid_index = rucksack.length() / 2;
    auto compartment_1 = rucksack.substr(0, mid_index);
    auto compartment_2 = rucksack.substr(mid_index);
    auto common_items = find_common_items(compartment_1, compartment_2);
    priority += get_priority(common_items[0]);
  }

  return priority;
}

//--------------------------------------------------------------------------------
unsigned int part2(const std::vector<std::string> &rucksacks) {
  unsigned int priority = 0;

  for (int i = 0; i < rucksacks.size(); i += 3) {
    auto elf_a = rucksacks[i];
    auto elf_b = rucksacks[i + 1];
    auto elf_c = rucksacks[i + 2];

    auto intersection_a_b = find_common_items(elf_a, elf_b);
    auto intersection_a_c = find_common_items(elf_a, elf_c);
    auto common_items = find_common_items(intersection_a_b, intersection_a_c);

    priority += get_priority(common_items[0]);
  }

  return priority;
}

//--------------------------------------------------------------------------------
int main() {
  std::vector<std::string> rucksacks;

  std::ifstream file(DAY);
  if (file) {
    std::string line;
    while (std::getline(file, line))
      rucksacks.push_back(line);

    file.close();
  }

  std::cout << "Part 1: " << part1(rucksacks) << std::endl;
  std::cout << "Part 2: " << part2(rucksacks) << std::endl;

  return 0;
}
