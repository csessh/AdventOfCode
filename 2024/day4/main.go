package main

import (
	"fmt"

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

func isMASX(r int, c int, data []string) bool {
	if data[r][c] != 'A' {
		panic("Nah")
	}

	w := len(data[0])
	h := len(data)

	var tl byte
	var br byte

	// top left
	if r-1 >= 0 && c-1 >= 0 {
		tl = data[r-1][c-1]
	}

	// bottom right
	if r+1 < h && c+1 < w {
		br = data[r+1][c+1]
	}

	if !(tl != br && (tl == 'M' || tl == 'S') && (br == 'M' || br == 'S')) {
		return false
	}

	var tr byte
	var bl byte

	// top right
	if r-1 >= 0 && c+1 < w {
		tr = data[r-1][c+1]
	}

	// bottom left
	if r+1 < h && c-1 >= 0 {
		bl = data[r+1][c-1]
	}

	if !(tr != bl && (tr == 'M' || tr == 'S') && (bl == 'M' || bl == 'S')) {
		return false
	}

	return true
}

func findXmas(r int, c int, data []string) int {
	if data[r][c] != 'X' {
		panic("It's not Xmas yet")
	}

	w := len(data[0])
	h := len(data)
	count := 0

	// up
	if r-3 >= 0 {
		if data[r-1][c] == 'M' && data[r-2][c] == 'A' && data[r-3][c] == 'S' {
			count += 1
		}
	}

	// down
	if r+3 < h {
		if data[r+1][c] == 'M' && data[r+2][c] == 'A' && data[r+3][c] == 'S' {
			count += 1
		}
	}

	// right
	if c+3 < w {
		if data[r][c+1] == 'M' && data[r][c+2] == 'A' && data[r][c+3] == 'S' {
			count += 1
		}
	}

	// left
	if c-3 >= 0 {
		if data[r][c-1] == 'M' && data[r][c-2] == 'A' && data[r][c-3] == 'S' {
			count += 1
		}
	}

	// top left
	if r-3 >= 0 && c-3 >= 0 {
		if data[r-1][c-1] == 'M' && data[r-2][c-2] == 'A' && data[r-3][c-3] == 'S' {
			count += 1
		}
	}

	// top right
	if r-3 >= 0 && c+3 < w {
		if data[r-1][c+1] == 'M' && data[r-2][c+2] == 'A' && data[r-3][c+3] == 'S' {
			count += 1
		}
	}

	// bottom left
	if r+3 < h && c-3 >= 0 {
		if data[r+1][c-1] == 'M' && data[r+2][c-2] == 'A' && data[r+3][c-3] == 'S' {
			count += 1
		}
	}

	// bottom right
	if r+3 < h && c+3 < w {
		if data[r+1][c+1] == 'M' && data[r+2][c+2] == 'A' && data[r+3][c+3] == 'S' {
			count += 1
		}
	}

	return count
}

func part1(data []string) int {
	count := 0

	for i, row := range data {
		for j, c := range row {
			if c == 'X' {
				count += findXmas(i, j, data)
			}
		}
	}

	return count
}

func part2(data []string) int {
	count := 0

	for i, row := range data {
		for j, c := range row {
			if c == 'A' && isMASX(i, j, data) {
				count += 1
			}
		}
	}

	return count
}
