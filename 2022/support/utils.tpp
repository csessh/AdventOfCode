#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <vector>

//--------------------------------------------------------------------------------
// declarations
//--------------------------------------------------------------------------------
template <typename T> T findCommonItems(T &left, T &right);
std::vector<std::string> split(const std::string &original, const std::string &delimiter);

//--------------------------------------------------------------------------------
// Template implementations
//--------------------------------------------------------------------------------
template <typename T> T findCommonItems(T &left, T &right) {
    /// @brief Find the intersection of two sets.
    /// @tparam T
    /// @param left
    /// @param right
    /// @return a set of common items
    T common_items;
    std::sort(left.begin(), left.end());
    std::sort(right.begin(), right.end());

    std::set_intersection(
        left.begin(),
        left.end(),
        right.begin(),
        right.end(),
        std::back_inserter(common_items));

    return common_items;
}

//--------------------------------------------------------------------------------
std::vector<std::string> split(const std::string &original, const std::string &delimiter) {
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

#endif