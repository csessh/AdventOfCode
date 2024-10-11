#include <fstream>
#include <iostream>
#include <map>

const std::string DAY = "input/day2";

const std::map<char, int> SHAPES = {
    {'X', 1}, // Rock
    {'Y', 2}, // Paper
    {'Z', 3}  // Scissors
};

const unsigned int WIN = 6;
const unsigned int DRAW = 3;
const unsigned int LOST = 0;

const std::map<char, unsigned int> POINTS = {
    {'X', LOST}, {'Y', DRAW}, {'Z', WIN}};

const std::map<char, char> WIN_STRATEGIES = {
    {'A', 'Y'}, {'B', 'Z'}, {'C', 'X'}};

const std::map<char, char> DRAW_STRATEGIES = {
    {'A', 'X'}, {'B', 'Y'}, {'C', 'Z'}};

const std::map<char, char> LOST_STRATEGIES = {
    {'A', 'Z'}, {'B', 'X'}, {'C', 'Y'}};

const std::map<char, std::map<char, char>> GUIDES = {
    {'X', LOST_STRATEGIES}, {'Y', DRAW_STRATEGIES}, {'Z', WIN_STRATEGIES}};

//--------------------------------------------------------------------------------
int fight(const char &opponent, const char &mine) {
  if (opponent == 'A' && mine == 'X')
    return DRAW;

  if (opponent == 'B' && mine == 'Y')
    return DRAW;

  if (opponent == 'C' && mine == 'Z')
    return DRAW;

  if (opponent == 'A' && mine == 'Y')
    return WIN;

  if (opponent == 'B' && mine == 'Z')
    return WIN;

  if (opponent == 'C' && mine == 'X')
    return WIN;

  return LOST;
}

//--------------------------------------------------------------------------------
unsigned int get_shape(const char &opponent, const char &guide) {
  char move = GUIDES.at(guide).at(opponent);
  return SHAPES.at(move);
}

//--------------------------------------------------------------------------------
unsigned int part2() {
  unsigned int score = 0;

  std::ifstream file(DAY);
  if (file) {
    std::string line;
    while (std::getline(file, line)) {
      score += POINTS.at(line[2]);
      score += get_shape(line[0], line[2]);
    }

    file.close();
  }

  return score;
}

//--------------------------------------------------------------------------------
unsigned int part1() {
  unsigned int score = 0;

  std::ifstream file(DAY);
  if (file) {
    std::string line;
    while (std::getline(file, line)) {
      score += SHAPES.at(line[2]);
      score += fight(line[0], line[2]);
    }

    file.close();
  }

  return score;
}

//--------------------------------------------------------------------------------
int main() {
  std::cout << "Part 1: " << part1() << std::endl;
  std::cout << "Part 2: " << part2() << std::endl;

  return 0;
}
