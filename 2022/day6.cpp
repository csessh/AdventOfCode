#include <iostream>
#include <fstream>
#include <set>

const std::string DAY = "input/day6";

//--------------------------------------------------------------------------------
const unsigned int scan_for_start_of_packet_marker(const std::string data, size_t size) {
    for (auto i=0; i < data.length()-size; i++) {
        std::set<char> uniques;
        uniques.insert(data[i]);

        for (auto j=1; j<size; j++) {
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
    auto marker_index = 0;

    std::ifstream file(DAY);
    if (file.is_open()) {
        std::string line;
        while (std::getline(file, line))
            marker_index = scan_for_start_of_packet_marker(line, 14);

        file.close();
    }

    std::cout << "Marker is at index " << marker_index << std::endl;

    return 0;
}