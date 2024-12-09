package main

import (
	"fmt"
	// "time"

	elf "github.com/csessh/AdeventOfCode/helpers"
	deepcopy "github.com/tiendc/go-deepcopy"
)

const (
	UP    = iota
	RIGHT = iota
	DOWN  = iota
	LEFT  = iota
)

type Location struct{ row, col int }
type Grid [][]byte
type Possibility struct {
	grid Grid
	loc  Location
	dir  int
}

func main() {
	data, err := elf.Slurp()
	if err != nil {
		panic(fmt.Sprintf("Unable to process input file: %v", err))
	}

	_data := make(Grid, 0, len(data))
	for _, line := range data {
		_data = append(_data, []byte(line))
	}

	l, d := pingSelf(_data)
	possibilities, steps := patrol(l, d, _data, true)

	possible_loops := 0
	for _, p := range possibilities {
		_, s := patrol(p.loc, p.dir, p.grid, false)
		if s == -1 {
			possible_loops += 1
		}
	}

	fmt.Printf("Part 1 = %d\n", steps)
	fmt.Printf("Part 2 = %d\n", possible_loops)
}

func pingSelf(data Grid) (Location, int) {
	for r, row := range data {
		for c, char := range row {
			if char == byte('^') {
				return Location{r, c}, UP
			}
		}
	}

	return Location{-1, -1}, UP
}

func display(data Grid) {
	fmt.Print("\033[H\033[2J")
	for _, line := range data {
		fmt.Println(string(line))
	}
}

func isVisistedPath(char byte) bool {
	return char == byte('^') || char == byte('V') || char == byte('<') || char == byte('>')
}

func isLooping(char byte, dir int) bool {
	return (char == byte('^') && dir == UP) ||
		(char == byte('V') && dir == DOWN) ||
		(char == byte('<') && dir == LEFT) ||
		(char == byte('>') && dir == RIGHT)
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

func patrol(start Location, direction int, data Grid, explore bool) ([]Possibility, int) {
	h := len(data)
	w := len(data[0])
	loc := start
	po := make([]Possibility, 0)

	// Very hacky
	limit := h * w * 5
	var next Location

	for {
		limit -= 1
		if limit <= 0 {
			return nil, -1
		}

		leaveTrail(&data[loc.row][loc.col], direction)
		next = getNextCoordinate(loc, direction)

		if next.row >= h || next.row < 0 || next.col >= w || next.col < 0 {
			break
		}

		if isLooping(data[next.row][next.col], direction) {
			return nil, -1
		}

		if data[next.row][next.col] == byte('#') {
			direction = (direction + 1) % 4
		} else {
			if explore && !isVisistedPath(data[next.row][next.col]) {
				var new_grid Grid
				err := deepcopy.Copy(&new_grid, &data)
				if err != nil {
					panic("Something wrong with deepcopy")
				}

				new_grid[next.row][next.col] = byte('#')
				possible := Possibility{
					grid: new_grid,
					loc:  loc,
					dir:  direction,
				}

				po = append(po, possible)
			}

			loc = next

			// display(data)
			// time.Sleep(20 * time.Millisecond)
		}
	}

	steps := 0
	for _, line := range data {
		for _, char := range line {
			if isVisistedPath(char) {
				steps += 1
			}
		}
	}

	return po, steps
}

func leaveTrail(mark *byte, dir int) {
	if dir == UP {
		*mark = byte('^')
	} else if dir == DOWN {
		*mark = byte('V')
	} else if dir == RIGHT {
		*mark = byte('>')
	} else if dir == LEFT {
		*mark = byte('<')
	}
}
