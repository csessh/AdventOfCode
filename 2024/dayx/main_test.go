package main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	want := 11

	if got := part1(); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart2(t *testing.T) {
	want := 31

	if got := part2(); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}
