package main

import (
	"testing"
)

var (
	left  = []int{3, 4, 2, 1, 3, 3}
	right = []int{4, 3, 5, 3, 9, 3}
)

func TestPart1(t *testing.T) {
	want := 11

	if got := part1(left, right); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart2(t *testing.T) {
	want := 31

	if got := part2(left, right); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}
