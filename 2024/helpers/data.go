package helper

import (
	"bufio"
	"os"
)

// Open and read puzzle input from puzzle.txt located in the same directory
// This helper elf function is the initial step in processing data
// by breaking them into a list of string to be further processed.
//
// Each line of input is stripped.
func Slurp() ([]string, error) {
	file, err := os.Open("puzzle.txt")
	if err != nil {
		return nil, err
	}

	data := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		data = append(data, scanner.Text())
	}

	err = file.Close()
	if err != nil {
		return nil, err
	}

	return data, nil
}
