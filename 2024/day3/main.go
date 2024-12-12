package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	elf "github.com/csessh/AdventOfCode/helpers"
)

func main() {
	data, err := elf.Slurp()
	if err != nil {
		panic(fmt.Sprintf("Unable to process input file: %v", err))
	}

	fmt.Printf("Part 1 = %d\n", part1(data))
	fmt.Printf("Part 2 = %d\n", part2(data))
}

func extract(memory string) int {
	re := regexp.MustCompile(`mul\(([0-9]+,[0-9]+)\)`)
	value := 0

	for _, input := range re.FindAllStringSubmatch(memory, -1) {
		numbers := strings.Split(input[1], ",")

		lhs, err := strconv.Atoi(numbers[0])
		if err != nil {
			panic("NaN")
		}

		rhs, err := strconv.Atoi(numbers[1])
		if err != nil {
			panic("NaN")
		}

		value += lhs * rhs
	}

	return value
}

func part1(corrupted_memories []string) int {
	result := 0

	for _, memory := range corrupted_memories {
		result += extract(memory)
	}

	return result
}

func part2(corrupted_memories []string) int {
	total := 0

	all := strings.Join(corrupted_memories, "")
	donts := strings.Split(all, "don't()")

	for i, dont := range donts {
		if i == 0 && len(dont) > 0 {
			// Anything before the very first don't() is still "enabled"
			total += extract(dont)
			continue
		}

		dos := strings.Split(dont, "do()")
		for j, do := range dos {
			// Between the first do() and the last don't() is "disabled"
			if j == 0 || len(do) == 0 {
				continue
			}

			total += extract(do)
		}
	}

	return total
}
