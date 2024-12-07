package main

import (
	"testing"
)

var sample = []string{
	"190: 10 19",
	"3267: 81 40 27",
	"83: 17 5",
	"156: 15 6",
	"7290: 6 8 6 15",
	"161011: 16 10 13",
	"192: 17 8 14",
	"21037: 9 7 18 13",
	"292: 11 6 16 20",
}

func TestProcess(t *testing.T) {
	test := "190: 10 19"
	want_test := 190
	want_nums := []int{10, 19}
	got_test, got_nums := process(test)

	if got_test != want_test {
		t.Errorf("got = %v, want %v", got_test, want_test)
	}

	for i, n := range got_nums {
		if n != want_nums[i] {
			t.Errorf("got = %v, want %v", n, want_nums[i])
		}
	}
}

func TestPart1(t *testing.T) {
	want := 3749

	if got := part1(sample); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart2(t *testing.T) {
	want := 11387 

	if got := part2(sample); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}
