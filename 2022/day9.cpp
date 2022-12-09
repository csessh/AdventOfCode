#include <iostream>
#include <fstream>
#include <cmath>
#include "utils.tpp"

const std::string DAY = "input/day9";

class Snake {
    public:
        std::pair<int, int> head;
        std::pair<int, int> tail;
        std::vector<std::pair<int, int>> trails;

        Snake() :
        head(std::pair<int, int>(0, 0)),
        tail(std::pair<int, int>(0, 0)) {
            trails.push_back(head);
        }

        void move_left(const int &steps) {
            for (auto i = 0; i < steps; i++) {
                head.first -= 1;

                if (is_tail_too_far_behind()) {
                    if (is_snakey_bent())
                        tail.second = head.second;
                    tail.first = head.first + 1;
                }

                if (find(trails.begin(), trails.end(), tail) == trails.end())
                    trails.push_back(tail);
            }
        }

        void move_right(const int &steps) {
            for (auto i = 0; i < steps; i++) {
                head.first += 1;

                if (is_tail_too_far_behind()) {
                    if (is_snakey_bent())
                        tail.second = head.second;
                    tail.first = head.first - 1;
                }

                if (find(trails.begin(), trails.end(), tail) == trails.end())
                    trails.push_back(tail);
            }
        }

        void move_up(const int &steps) {
            for (auto i = 0; i < steps; i++) {
                head.second += 1;

                if (is_tail_too_far_behind()) {
                    if (is_snakey_bent())
                        tail.first = head.first;
                    tail.second = head.second - 1;
                }

                if (find(trails.begin(), trails.end(), tail) == trails.end())
                    trails.push_back(tail);
            }
        }

        void move_down(const int &steps) {
            for (auto i = 0; i < steps; i++) {
                head.second -= 1;

                if (is_tail_too_far_behind()) {
                    if (is_snakey_bent())
                        tail.first = head.first;
                    tail.second = head.second + 1;
                }

                if (find(trails.begin(), trails.end(), tail) == trails.end())
                    trails.push_back(tail);
            }
        }
    private:
        bool is_tail_too_far_behind() {
            auto max_distance = 2;
            if (is_snakey_bent())
                max_distance = 3;

            return (abs(head.first - tail.first) + abs(head.second - tail.second)) >= max_distance;
        }

        bool is_snakey_bent() {
            return (head.first != tail.first && head.second != tail.second);
        }
};

//--------------------------------------------------------------------------------
int main() {
    Snake snake;

    std::ifstream file(DAY);
    if (file) {
        std::string line;
        while (std::getline(file, line)) {
            auto steps = std::atoi(&line[1]);

            if (line[0] == 'R')
                snake.move_right(steps);
            else if (line[0] == 'L')
                snake.move_left(steps);
            else if (line[0] == 'U')
                snake.move_up(steps);
            else if (line[0] == 'D')
                snake.move_down(steps);
        }
        file.close();
    }

    std::cout << "Part 1: " << snake.trails.size() << " positions visited at least once" << std::endl;
    return 0;
}