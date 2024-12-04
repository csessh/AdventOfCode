package main

import (
	"testing"
)

var sample = []string {
	"test",
}

func TestPart1(t *testing.T) {
	want := 0

	if got := part1(sample); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart2(t *testing.T) {
	want := 0

	if got := part2(sample); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}
