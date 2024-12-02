package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"

	elf "github.com/csessh/AdeventOfCode/helpers"
)

func main() {
	data, err := elf.Slurp()
	if err != nil {
		panic(fmt.Sprintf("Unable to process input file: %v", err))
	}

	process(data)
	part1()

	process(data)
	part2()
}

func process(data []string) { }

func part1() { }

func part2() { }
