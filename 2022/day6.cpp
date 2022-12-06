#include <iostream>
#include <fstream>
#include <set>

const std::string DAY = "input/day6";

//--------------------------------------------------------------------------------
unsigned int get_marker_index(const std::string data, size_t size) {
    for (auto i = 0; i < data.length()-size; i++) {
        std::set<char> uniques;

        for (auto j = 0; j < size; j++) {
            if (uniques.find(data[i+j]) == uniques.end())
                uniques.insert(data[i+j]);
        }

        if (uniques.size() == size)
            return i+size;
    }

    return 0;
}

//--------------------------------------------------------------------------------
int main() {
    std::ifstream file(DAY);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line))
            std::cout << "Marker is at index " << get_marker_index(line, 14) << std::endl;

        file.close();
    }


    return 0;
}