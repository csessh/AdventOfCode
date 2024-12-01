#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <regex>
#include <vector>

const std::string DAY = "input/day7";

struct Directory;

//--------------------------------------------------------------------------------
struct File {
  std::string name;
  size_t size;
  Directory *pParent;
};

struct Directory {
  std::string name;
  std::map<std::string, File *> files;
  std::map<std::string, Directory *> directories;
  Directory *pParent;
  size_t size;
};

//--------------------------------------------------------------------------------
void cd(Directory *&pPWD, const std::string &name) {
  if (!pPWD) {
    pPWD = new Directory();
    pPWD->name = name;
    pPWD->size = 0;
    pPWD->pParent = NULL;
  } else {
    if (name == ".." && pPWD->pParent) {
      pPWD = pPWD->pParent;
    } else if (pPWD->directories[name]) {
      pPWD = pPWD->directories.at(name);
    } else {
      auto pNew = new Directory();
      pNew->pParent = pPWD;
      pNew->name = name;
      pPWD->directories.insert(std::pair<std::string, Directory *>(name, pNew));
      pPWD = pNew;
    }
  }
}

//--------------------------------------------------------------------------------
void construct(std::queue<std::string> &commands, Directory *&pRoot) {
  auto in_ls_mode = false;
  Directory *pPWD = pRoot;

  while (!commands.empty()) {
    auto command = commands.front();
    commands.pop();

    std::smatch matches;
    if (std::regex_search(command, matches, std::regex("\\$ cd (.+)"))) {
      in_ls_mode = false;
      cd(pPWD, matches[1]);
    } else if (command == "$ ls") {
      in_ls_mode = true;
    }

    if (in_ls_mode) {
      if (std::regex_search(command, matches, std::regex("^dir (.+)$"))) {
        auto pNew = new Directory();
        pNew->name = matches[1];
        pNew->pParent = pPWD;
        pPWD->directories.insert(
            std::pair<std::string, Directory *>(matches[1], pNew));
      } else if (std::regex_search(command, matches,
                                   std::regex("^([0-9]+) (.+)$"))) {
        auto pNew = new File();
        pNew->name = matches[2];
        pNew->size = std::stoi(matches[1]);
        pNew->pParent = pPWD;

        auto pDir = pNew->pParent;
        while (pDir) {
          pDir->size += pNew->size;
          pDir = pDir->pParent;
        }
      }
    }
  }
}

//--------------------------------------------------------------------------------
int part1(Directory *&pRoot) {
  auto size = 0;

  std::queue<Directory *> dir;
  dir.push(pRoot);

  while (!dir.empty()) {
    auto pCurrent = dir.front();
    dir.pop();

    if (pCurrent->size <= 100000)
      size += pCurrent->size;

    for (auto &sub : pCurrent->directories)
      dir.push(sub.second);
  }

  return size;
}

//--------------------------------------------------------------------------------
int part2(Directory *&pRoot) {
  auto MAX = 70000000;
  auto REQUIRED = 30000000;
  auto free = MAX - pRoot->size;

  std::vector<int> sizes;
  std::queue<Directory *> dir;
  dir.push(pRoot);

  while (!dir.empty()) {
    auto pCurrent = dir.front();
    dir.pop();

    sizes.push_back(pCurrent->size);

    for (auto &sub : pCurrent->directories)
      dir.push(sub.second);
  }

  std::sort(sizes.begin(), sizes.end());
  for (auto size : sizes) {
    if (free + size >= REQUIRED)
      return size;
  }

  return 0;
}

//--------------------------------------------------------------------------------
int main() {
  std::queue<std::string> commands;

  std::ifstream file(DAY);
  if (file) {
    std::string line;
    while (std::getline(file, line))
      commands.push(line);

    file.close();
  }

  commands.pop();
  auto pRoot = new Directory();
  pRoot->name = "/";
  pRoot->size = 0;
  pRoot->pParent = NULL;
  construct(commands, pRoot);

  std::cout << "Part 1: Total size = " << part1(pRoot) << std::endl;
  std::cout << "Part 2: Total size = " << part2(pRoot) << std::endl;

  return 0;
}
