package main

import (
	"fmt"
	"slices"
	"sort"
	"strconv"
	"strings"

	elf "github.com/csessh/AdventOfCode/helpers"
)

func main() {
	data, err := elf.Slurp()
	if err != nil {
		panic(fmt.Sprintf("Unable to process input file: %v", err))
	}

	rules, updates := extractRulesAndUpdates(data)
	good, bad := calculate(rules, updates)

	fmt.Printf("Part 1 = %d\n", good)
	fmt.Printf("Part 2 = %d\n", bad)
}

func getMiddleNumber(update []int) int {
	if len(update)%2 != 1 {
		panic("Order size is even, not odd")
	}

	m := len(update) / 2
	return update[int(m)]
}

func extractRulesAndUpdates(data []string) (map[int][]int, [][]int) {
	rules := make(map[int][]int)
	updates := make([][]int, 0)
	for i := range updates {
		updates[i] = make([]int, 0)
	}

	is_parsing_rules := true
	for _, line := range data {
		if line == "" {
			is_parsing_rules = false
			continue
		}

		if is_parsing_rules {
			splits := strings.Split(line, "|")

			lhs, err1 := strconv.Atoi(splits[0])
			rhs, err2 := strconv.Atoi(splits[1])

			if err1 != nil || err2 != nil {
				panic("Something went wrong here")
			}

			rules[lhs] = append(rules[lhs], rhs)
		} else {
			splits := strings.Split(line, ",")
			update := make([]int, 0, len(splits))

			for _, i := range splits {
				n, err := strconv.Atoi(i)
				if err != nil {
					panic("Something also went wrong here")
				}

				update = append(update, n)
			}

			updates = append(updates, update)
		}
	}

	return rules, updates
}

func gt(a int, b int, rules map[int][]int) bool {
	return slices.Contains(rules[a], b)
}

func calculate(rules map[int][]int, updates [][]int) (int, int) {
	good_result := 0
	bad_result := 0

	for _, update := range updates {
		good := true

		for i, page := range update {
			if i == len(update)-1 {
				break
			}

			if !gt(page, update[i+1], rules) {
				good = false
				break
			}
		}

		if good {
			good_result += getMiddleNumber(update)
		} else {
			sort.SliceStable(update, func(i, j int) bool {
				return gt(update[i], update[j], rules)
			})
			bad_result += getMiddleNumber(update)
		}
	}

	return good_result, bad_result
}
