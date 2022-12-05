#include <iostream>
#include <fstream>
#include <vector>
#include "helper.h"

const std::string DAY = "input/day4";

//--------------------------------------------------------------------------------
int main() {
    std::vector<std::string> assignments = {};

    std::ifstream file(DAY);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            assignments.push_back(line);
        }
        file.close();
    }

    unsigned int part1 = 0;
    unsigned int part2 = 0;

    for (const auto& pair : assignments) {
        auto instructions = split(pair, ",");
        auto elf_a = instructions[0];
        auto elf_b = instructions[1];

        auto elf_a_instructions = split(elf_a, "-");
        auto elf_a_start = std::stoi(elf_a_instructions[0]);
        auto elf_a_end = std::stoi(elf_a_instructions[1]);

        auto elf_b_instructions = split(elf_b, "-");
        auto elf_b_start = std::stoi(elf_b_instructions[0]);
        auto elf_b_end = std::stoi(elf_b_instructions[1]);

        if ((elf_a_start <= elf_b_start && elf_a_end >= elf_b_end) || (elf_b_start <= elf_a_start && elf_b_end >= elf_a_end))
            part1 += 1;

        if ((elf_a_end <= elf_b_end && elf_a_end >= elf_b_start) || (elf_b_end <= elf_a_end && elf_b_end >= elf_a_start))
            part2 += 1;
    }

    std::cout << "Part 1: " << part1 << std::endl;
    std::cout << "Part 2: " << part2 << std::endl;

    return 0;
}