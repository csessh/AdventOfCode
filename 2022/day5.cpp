#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <regex>
#include <stdlib.h>
#include <unistd.h>
#include "helper.h"

typedef std::vector<std::string> Instructions;
typedef std::vector<std::string> Crates;

const std::string DAY = "input/day5";

//--------------------------------------------------------------------------------
class CargoCrane {
public:
    std::map<unsigned int, Crates*> stacks;
    size_t size;

    CargoCrane(const std::string &labels) {
        std::smatch match;

        // Labels are organised in ascending order from left to right.
        // For example:  1   2   3 ... 100
        // 100 would be the size of this Cargo ship
        if (std::regex_search(labels, match, std::regex("([0-9]+)\\s*$")))
            this->size = std::stoi(match[1]);

        for (auto i = 1; i <= this->size; i++)
            this->stacks[i] = new Crates();
    }

    ~CargoCrane() {
        std::cout << "Sinking the cargo ship ... bye!" << std::endl;
        for (auto i = 1; i <= this->size; i++)
            delete this->stacks[i];
    }

    /// @brief Part 1 requires a read of all labels of the top creates on each stack
    void read_top_labels() {
        std::cout << "Top labels: ";
        for (const auto& stack : stacks)
            std::cout << stack.second->back()[1];
        std::cout << std::endl;
    }

    /// @brief Display the current state of the Cargo ship on screen
    /// @param pretty Crates are presented in horizontal by default. Vertical stacks are prettier
    void draw() {
        for (const auto& stack: this->stacks) {
            std::cout << stack.first << ": ";
            for (auto&& crate : *stack.second) {
                std::cout << crate << " ";
            }
            std::cout << std::endl;
        }
        std::cout << std::endl;
    }

    /// @brief Crates are loaded and sorted into their appropriate stacks
    /// @param crates Crates come in batch i.e. [Z] [M] [P]
    void load(const std::string &crates) {
        auto index = 0;

        for (auto i = 1; i <= this->size; i++) {
            if (index > crates.length())
                break;

            auto crate = crates.substr(index, 3);

            if (crate != "   ")
                this->stacks.at(i)->push_back(crate);

            index += 4;
        }
    }

    /// @brief Take a single line of command and execute.
    /// @param command i.e. "move 26 from 1 to 7"
    void execute(const std::string &command, bool reserve_order=false) {
        std::smatch matches;

        unsigned int quantity = 0;
        unsigned int source = 0;
        unsigned int destination = 0;

        if (std::regex_search(command, matches, std::regex("move ([0-9]+) from ([0-9]+) to ([0-9]+)"))) {
            quantity = std::stoi(matches[1].str());
            source = std::stoi(matches[2].str());
            destination = std::stoi(matches[3].str());
        }

        if (!reserve_order)
            this->move(quantity, source, destination);
        else
            this->ordered_move(quantity, source, destination);
    }

private:
    void ordered_move(unsigned int &quantity, unsigned int &source, unsigned int &destination) {
        Crates temp = {};
        for (auto i = 0; i < quantity; i++) {
            auto crate = this->stacks[source]->back();
            this->stacks[source]->pop_back();
            temp.push_back(crate);
        }

        std::reverse(temp.begin(), temp.end());

        for (const auto& crate : temp)
            this->stacks[destination]->push_back(crate);
    }

    void move(unsigned int &quantity, unsigned int &source, unsigned int &destination) {
        for (auto i = 0; i < quantity; i++) {
            auto crate = this->stacks[source]->back();
            this->stacks[source]->pop_back();
            this->stacks[destination]->push_back(crate);
        }
    }
};

//--------------------------------------------------------------------------------
void process(const Instructions &instructions, const Crates &data, const std::string &labels, bool reserve_order=false) {
    auto pCargo = new CargoCrane(labels);

    for (const auto& intake : data)
        pCargo->load(intake);

    pCargo->draw();
    for (const auto& command : instructions) {
        system("clear");

        std::cout << "Executing: " << command << std::endl;
        std::cout << std::endl;

        pCargo->execute(command, reserve_order);
        pCargo->draw();

        sleep(1);
    }

    pCargo->read_top_labels();
    delete pCargo;
}


//--------------------------------------------------------------------------------
int main() {
    Crates data = {};
    Instructions commands = {};
    auto is_cargo_loaded = false;

    std::ifstream file(DAY);
    if (file) {
        std::string line;
        while (std::getline(file, line)) {
            if (line.empty()) {
                is_cargo_loaded = true;
                continue;
            }

            if (!is_cargo_loaded)
                data.push_back(line);
            else
                commands.push_back(line);
        }
        file.close();
    }

    auto labels = data.back();
    data.pop_back();

    // reverse the order of input to simulate a queue of incoming crates for the ship to load.
    std::reverse(data.begin(), data.end());

    // Part 1
    process(commands, data, labels, false);

    // Part 2
    process(commands, data, labels, true);

    return 0;
}