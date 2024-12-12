package main

import (
	"fmt"
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

	left, right := process(data)
	part1(left, right)

	left, right = process(data)
	part2(left, right)
}

func process(data []string) ([]int, []int) {
	left := []int{}
	right := []int{}

	for _, item := range data {
		ids := strings.Split(item, "   ")
		l, err := strconv.Atoi(ids[0])
		if err != nil {
			panic(fmt.Sprintf("Unable to process input file: %v", err))
		}

		r, err := strconv.Atoi(ids[1])
		if err != nil {
			panic(fmt.Sprintf("Unable to process input file: %v", err))
		}

		left = append(left, l)
		right = append(right, r)
	}

	return left, right
}

func part1(left []int, right []int) int {
	sort.Ints(left)
	sort.Ints(right)

	total := 0
	for i, loc := range left {
		diff := loc - right[i]
		total += max(diff, -diff)
	}

	fmt.Printf("Part 1: %d \n", total)
	return total
}

func part2(left []int, right []int) int {
	score := 0
	counter := make(map[int]int)

	for _, loc := range right {
		counter[loc] += 1
	}

	for _, loc := range left {
		score += loc * counter[loc]
	}

	fmt.Printf("Part 2: %d \n", score)
	return score
}
