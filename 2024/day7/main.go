package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"

	elf "github.com/csessh/AdeventOfCode/helpers"
)

func main() {
	data, err := elf.Slurp()
	if err != nil {
		panic(fmt.Sprintf("Unable to process input file: %v", err))
	}

	fmt.Printf("Part 1 = %d\n", calibrate(data, false))
	fmt.Printf("Part 2 = %d\n", calibrate(data, true))
}

func process(equation string) (int, []int) {
	s := strings.Split(equation, ": ")
	n := strings.Split(s[1], " ")

	test, _ := strconv.Atoi(s[0])
	numbers := make([]int, 0, len(n))

	for _, n := range n {
		i, _ := strconv.Atoi(n)
		numbers = append(numbers, i)
	}

	return test, numbers
}

func crunch(val int, numbers []int, concat bool) []int {
	subset := make([]int, 0)

	if len(numbers) == 0 {
		return []int{val}
	}

	add := val + numbers[0]
	mul := val * numbers[0]

	subset = append(subset, crunch(add, numbers[1:], concat)...)
	subset = append(subset, crunch(mul, numbers[1:], concat)...)

	if concat {
		log10 := int(math.Log10(float64(numbers[0])))
		con := val*int(math.Pow10(log10+1)) + numbers[0]
		subset = append(subset, crunch(con, numbers[1:], concat)...)
	}

	return subset
}

func calibrate(data []string, concat bool) int {
	total := 0
	for _, line := range data {
		test, numbers := process(line)

		possible_values := crunch(numbers[0], numbers[1:], concat)
		for _, val := range possible_values {
			if val == test {
				total += test
				break
			}
		}

	}

	return total
}
