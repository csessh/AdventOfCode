#include <fstream>
#include <iostream>
#include <vector>

const std::string DAY = "input/day1";

//--------------------------------------------------------------------------------
int main() {
  std::vector<unsigned int> elves = {};
  unsigned int current_count = 0;

  std::ifstream file(DAY);
  if (file) {
    std::string line;
    while (std::getline(file, line)) {
      if (line.empty()) {
        elves.push_back(current_count);
        current_count = 0;
        continue;
      }

      current_count += std::stoi(line);
    }
    file.close();
  }

  std::sort(elves.begin(), elves.end(), std::greater<int>());

  std::cout << "Part 1: " << elves[0] << std::endl;
  std::cout << "Part 2: " << elves[0] + elves[1] + elves[2] << std::endl;

  return 0;
}
