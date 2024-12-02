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

func convertLevelsToInt(levels string) []int {
	report := make([]int, 0, len(strings.Split(levels, " ")))

	for _, val := range strings.Split(levels, " ") {
		v, err := strconv.Atoi(val)
		if err != nil {
			panic(fmt.Sprintf("Unexpected value in puzzle input: %v", err))
		}

		report = append(report, v)
	}

	return report
}

func isSafe(levels []int) bool {
	first_level := levels[0]
	second_level := levels[1]
	is_level_rising := (second_level - first_level) > 0

	for i, level := range levels {
		if i == 0 {
			continue
		}

		prev := levels[i-1]
		diff := level - prev

		if max(diff, -diff) > 3 || max(diff, -diff) < 1 {
			return false
		}

		if diff > 0 != is_level_rising {
			return false
		}
	}

	return true
}

func part1(data []string) (int, []string) {
	safe_report_counter := 0
	var bad_reports []string

	for _, row := range data {
		report := convertLevelsToInt(row)

		if isSafe(report) {
			safe_report_counter += 1
		} else {
			bad_reports = append(bad_reports, row)
		}
	}

	return safe_report_counter, bad_reports
}

func part2(data []string) int {
	fixables := 0

	for _, row := range data {
		report := convertLevelsToInt(row)

		for i := range report {
			attempt := make([]int, 0, len(report)-1)
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
