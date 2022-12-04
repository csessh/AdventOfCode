#ifndef UTILS_H
#define UTILS_H

#include <iostream>


template <typename T>
T findCommonItems(T &left, T &right);


template <typename T>
T findCommonItems(T &left, T &right) {
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