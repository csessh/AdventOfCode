#include "helper.h"
#include <iostream>
#include <vector>

//--------------------------------------------------------------------------------------------
std::vector<std::string> split(const std::string &original, const std::string &delimiter) {
    /// @brief This is literally the equivalent of Python split()
    /// @param original
    /// @param delimiter
    /// @return an array/vector of strings splitted from the original
    std::vector<std::string> tokens;

    for (size_t start = 0, end; start < original.length(); start = end + delimiter.length()) {
        size_t position = original.find(delimiter, start);
        if (position != std::string::npos)
            end = position;
        else
            end = original.length();

        std::string token = original.substr(start, end - start);
        if (!token.empty())
            tokens.push_back(token);
    }

    if (original.empty() || (original.size() >= delimiter.size() && original.substr(original.size() - delimiter.size()) == delimiter))
        tokens.push_back("");

    return tokens;
}