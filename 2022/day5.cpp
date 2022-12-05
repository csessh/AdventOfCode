#include <iostream>
#include <fstream>
#include <vector>
#include "helper.h"

const std::string DAY = "input/day5";

//--------------------------------------------------------------------------------
int main() {
    std::vector<std::string> data = {};

    std::ifstream file(DAY);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line)) {
            data.push_back(line);
        }
        file.close();
    }

    // std::cout << "Part 1: " << part1 << std::endl;
    // std::cout << "Part 2: " << part2 << std::endl;

    return 0;
}