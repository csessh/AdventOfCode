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

	fmt.Printf("Part 1 = %d\n", part1(data))
	fmt.Printf("Part 2 = %d\n", part2(data))
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
		fmt.Println(val)
		return []int{val}
	}

	add := val + numbers[0]
	mul := val * numbers[0]

	fmt.Println(val, "+", numbers, "=", add)
	subset = append(subset, crunch(add, numbers[1:], concat)...)
	fmt.Println(val, "*", numbers, "*", mul)
	subset = append(subset, crunch(mul, numbers[1:], concat)...)

	if concat {
		log10 := int(math.Log10(float64(numbers[0])))
		con := (val * int(math.Pow10(log10+1))) + numbers[0]
		fmt.Println(val, "|", numbers, "=", con)
		subset = append(subset, crunch(con, numbers[1:], concat)...)
	}

	return subset
}

func part1(data []string) int {
	total := 0
	for _, line := range data {
		test, numbers := process(line)
		fmt.Println(test, numbers)

		possible_values := make([]int, 0)
		possible_values = append(possible_values, crunch(numbers[0], numbers[1:], false)...)

		for _, val := range possible_values {
			if val == test {
				total += test
				break
			}
		}

		fmt.Println("Possible values: ", len(possible_values), possible_values)
	}

	return total
}

func part2(data []string) int {
	total := 0
	for _, line := range data {
		test, numbers := process(line)
		fmt.Println(test, numbers)

		possible_values := make([]int, 0)
		possible_values = append(possible_values, crunch(numbers[0], numbers[1:], true)...)

		for _, val := range possible_values {
			if val == test {
				total += test
				break
			}
		}

		fmt.Println("Possible values: ", len(possible_values), possible_values)
	}

	return total
}
