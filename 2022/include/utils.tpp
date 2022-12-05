#ifndef UTILS_H
#define UTILS_H

#include <iostream>
#include <vector>

//--------------------------------------------------------------------------------
// declarations
//--------------------------------------------------------------------------------
template <typename T> T find_common_items(T &left, T &right);

//--------------------------------------------------------------------------------
// Template implementations
//--------------------------------------------------------------------------------
template <typename T> T find_common_items(T &left, T &right) {
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

#endif