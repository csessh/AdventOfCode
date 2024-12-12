package main

import (
	"fmt"

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

func part1(data []string) int {
	return 0
}

func part2(data []string) int {
	return 0
}
