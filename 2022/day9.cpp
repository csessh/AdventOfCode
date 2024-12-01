#include "utils.tpp"
#include <cmath>
#include <fstream>
#include <iostream>

typedef std::pair<int, int> Location;
const std::string DAY = "input/day9";

//--------------------------------------------------------------------------------
class BodyPart {
public:
  Location location;
  BodyPart *pNext;
  unsigned int id;
  std::vector<std::pair<int, int>> trails;

  BodyPart(const unsigned int &pos = 0) : location(Location(0, 0)) {
    id = pos;
    trails.push_back(location);

    if (id < 9)
      pNext = new BodyPart(id + 1);
  }

  ~BodyPart() {
    if (pNext)
      delete pNext;
  }

  void left() {
    location.first -= 1;

    if (find(trails.begin(), trails.end(), location) == trails.end())
      trails.push_back(location);

    if (is_next_body_part_too_far_behind())
      pull();
  }

  void right() {
    location.first += 1;

    if (find(trails.begin(), trails.end(), location) == trails.end())
      trails.push_back(location);

    if (is_next_body_part_too_far_behind())
      pull();
  }

  void up() {
    location.second += 1;

    if (find(trails.begin(), trails.end(), location) == trails.end())
      trails.push_back(location);

    if (is_next_body_part_too_far_behind())
      pull();
  }

  void down() {
    location.second -= 1;

    if (find(trails.begin(), trails.end(), location) == trails.end())
      trails.push_back(location);

    if (is_next_body_part_too_far_behind())
      pull();
  }

private:
  void pull() {
    if (!is_next_body_part_too_far_behind())
      return;

    if (abs(location.first - pNext->location.first) >
        abs(location.second - pNext->location.second)) {
      pNext->location.second = location.second;
      horizontal_pull();
    } else if (abs(location.first - pNext->location.first) <
               abs(location.second - pNext->location.second)) {
      pNext->location.first = location.first;
      vertical_pull();
    } else {
      pNext->location.first = (location.first + pNext->location.first) / 2;
      vertical_pull();
    }
  }

  void horizontal_pull() {
    if (location.first > pNext->location.first)
      pNext->right();
    else
      pNext->left();
  }

  void vertical_pull() {
    if (location.second > pNext->location.second)
      pNext->up();
    else
      pNext->down();
  }

  bool is_next_body_part_too_far_behind() {
    if (!pNext)
      return false;

    auto max = 2;
    if (is_snakey_bendy())
      max = 3;

    return (abs(location.first - pNext->location.first) +
            abs(location.second - pNext->location.second)) >= max;
  }

  bool is_snakey_bendy() {
    if (!pNext)
      return false;

    return (location.first != pNext->location.first &&
            location.second != pNext->location.second);
  }
};

//--------------------------------------------------------------------------------
class Snake {
public:
  BodyPart *pHead;

  Snake() : pHead(new BodyPart()) {}

  ~Snake() {
    if (pHead)
      delete pHead;
  }

  void move(const std::string &command) {
    std::cout << command << std::endl;

    auto steps = std::atoi(&command[1]);

    for (auto i = 0; i < steps; i++) {
      if (command[0] == 'R')
        pHead->right();
      else if (command[0] == 'L')
        pHead->left();
      else if (command[0] == 'U')
        pHead->up();
      else if (command[0] == 'D')
        pHead->down();
    }
    draw();
    std::cout << std::endl;
  }

private:
  void draw() {
    BodyPart *pCurrent = pHead;
    while (pCurrent) {
      std::cout << "Part #" << pCurrent->id << " visited "
                << pCurrent->trails.size() << " places at least once"
                << std::endl;
      pCurrent = pCurrent->pNext;
    }
  }
};

//--------------------------------------------------------------------------------
int main() {
  Snake snake;

  std::ifstream file(DAY);
  if (file) {
    std::string line;
    while (std::getline(file, line))
      snake.move(line);

    file.close();
  }
  return 0;
}
