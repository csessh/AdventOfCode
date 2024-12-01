#include <fstream>
#include <iostream>
#include <vector>

const std::string DAY = "input/day8";

//--------------------------------------------------------------------------------
std::pair<bool, unsigned int>
check_visibility(const std::vector<std::string> &forrest,
                 const std::pair<int, int> location) {
  // Sideways
  auto col = location.first;
  auto row = location.second;
  auto height = forrest[col][row];
  auto score = 1;

  // North
  auto north = true;
  auto count = 0;
  for (auto i = col - 1; i >= 0; i--) {
    count += 1;
    if (height - forrest[i][row] <= 0) {
      north = false;
      break;
    }
  }
  score *= count;

  // South
  auto south = true;
  count = 0;
  for (auto i = col + 1; i < forrest.size(); i++) {
    count += 1;
    if (height - forrest[i][row] <= 0) {
      south = false;
      break;
    }
  }
  score *= count;

  // East
  auto east = true;
  count = 0;
  for (auto i = row - 1; i >= 0; i--) {
    count += 1;
    if (height - forrest[col][i] <= 0) {
      east = false;
      break;
    }
  }
  score *= count;

  // West
  auto west = true;
  count = 0;
  for (auto i = row + 1; i < forrest.front().size(); i++) {
    count += 1;
    if (height - forrest[col][i] <= 0) {
      west = false;
      break;
    }
  }
  score *= count;

  return std::pair<bool, unsigned int>((north || east || south || west), score);
}

//--------------------------------------------------------------------------------
int main() {
  std::vector<std::string> forrest;
  unsigned int visible_trees_count = 0;

  std::ifstream file(DAY);
  if (file) {
    std::string line;
    while (std::getline(file, line))
      forrest.push_back(line);
  }

  auto top = 0;
  for (auto col = 0; col < forrest.size(); col++) {
    for (auto row = 0; row < forrest.back().size(); row++) {
      auto tree = check_visibility(forrest, std::pair<int, int>(col, row));
      if (tree.first)
        visible_trees_count += 1;

      if (tree.second > top)
        top = tree.second;
    }
  }

  std::cout << "Part 1: " << visible_trees_count << " trees are visible"
            << std::endl;
  std::cout << "Part 2: Best tree has scenic score of " << top << std::endl;
  return 0;
}
