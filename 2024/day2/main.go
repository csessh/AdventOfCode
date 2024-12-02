package main

import (
	"fmt"
	"strconv"
	"strings"

	elf "github.com/csessh/AdeventOfCode/helpers"
)

func main() {
	data, err := elf.Slurp()
	if err != nil {
		panic(fmt.Sprintf("Unable to process input file: %v", err))
	}

	count, bad_reports := part1(data)
	fmt.Printf("Part 1: %d\n", count)

	actual_count := part2(bad_reports) + count
	fmt.Printf("Part 2: %d\n", actual_count)
}

func isSafe(levels []string) bool {
	first_level, err := strconv.Atoi(levels[0])
	if err != nil {
		panic(fmt.Sprintf("Unexpected value in puzzle input: %v", err))
	}

	second_level, err := strconv.Atoi(levels[1])
	if err != nil {
		panic(fmt.Sprintf("Unexpected value in puzzle input: %v", err))
	}

	is_level_rising := (second_level - first_level) > 0

	for i, level := range levels {
		if i == 0 {
			continue
		}

		val, err := strconv.Atoi(level)
		if err != nil {
			panic(fmt.Sprintf("Unexpected value in puzzle input: %v", err))
		}

		prev, err := strconv.Atoi(levels[i-1])
		if err != nil {
			panic(fmt.Sprintf("Unexpected value in puzzle input: %v", err))
		}

		if max(val-prev, prev-val) > 3 || max(val-prev, prev-val) < 1 {
			return false
		}

		diff := val - prev
		if diff > 0 != is_level_rising {
			return false
		}
	}

	return true
}

func part1(data []string) (int, []string) {
	safe_report_counter := 0
	var bad_reports []string

	for _, levels := range data {
		report := strings.Split(levels, " ")
		if isSafe(report) {
			safe_report_counter += 1
		} else {
			bad_reports = append(bad_reports, levels)
		}
	}

	return safe_report_counter, bad_reports
}

func part2(data []string) int {
	fixables := 0

	for _, levels := range data {
		report := strings.Split(levels, " ")

		for i := range report {
			attempt := make([]string, 0, len(report)-1)
			attempt = append(attempt, report[:i]...)
			attempt = append(attempt, report[i+1:]...)

			if isSafe(attempt) {
				fixables += 1
				break
			}
		}
	}

	return fixables
}
