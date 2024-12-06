package main

import (
	"fmt"

	elf "github.com/csessh/AdeventOfCode/helpers"
)

const (
	UP    = iota
	RIGHT = iota
	DOWN  = iota
	LEFT  = iota
)

type Location struct {
	row, col int
}

func main() {
	data, err := elf.Slurp()
	if err != nil {
		panic(fmt.Sprintf("Unable to process input file: %v", err))
	}

	_data := make([][]byte, 0, len(data))
	for _, line := range data {
		_data = append(_data, []byte(line))
	}

	steps, blockages := patrol(_data)

	fmt.Printf("Part 1 = %d\n", steps)
	fmt.Printf("Part 2 = %d\n", blockages)
}

func pingSelf(data [][]byte) Location {
	for r, row := range data {
		for c, char := range row {
			if char == byte('^') {
				return Location{r, c}
			}
		}
	}

	return Location{-1, -1}
}

func display(data [][]byte) {
	for _, line := range data {
		fmt.Println(string(line))
	}

	fmt.Println()
}

func isVisistedPath(char byte) bool {
	return char == byte('^') || char == byte('V') || char == byte('<') || char == byte('>')
}

func getNextCoordinate(loc Location, d int) Location {
	r := loc.row
	c := loc.col

	if d == UP {
		r -= 1
	} else if d == DOWN {
		r += 1
	} else if d == LEFT {
		c -= 1
	} else {
		c += 1
	}

	return Location{r, c}
}

func branchCanCreateLoop(location Location, direction int, data[][]byte) bool {
	turns := 0

	if turns == 4 {
		return true
	}

	return false
}

func patrol(data [][]byte) (int, int) {
	location := pingSelf(data)
	direction := UP
	height := len(data)
	width := len(data[0])
	potential_loops := 0

	for {
		if direction == UP {
			data[location.row][location.col] = byte('^')
		} else if direction == DOWN {
			data[location.row][location.col] = byte('V')
		} else if direction == RIGHT {
			data[location.row][location.col] = byte('>')
		} else if direction == LEFT {
			data[location.row][location.col] = byte('<')
		}

		next := getNextCoordinate(location, direction)
		if next.row >= height || next.row < 0 || next.col >= width || next.col < 0 {
			break
		} else if data[next.row][next.col] == byte('#') {
			direction = (direction + 1) % 4
		} else {
			if branchCanCreateLoop(location, direction, data) {
				potential_loops += 1
			}

			location = next
		}

	}

	step := 0
	for _, line := range data {
		for _, char := range line {
			if isVisistedPath(char) {
				step += 1
			}
		}
	}

	display(data)
	return step, potential_loops
}
