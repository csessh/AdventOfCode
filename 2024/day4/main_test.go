package main

import (
	"testing"
)

var sample = []string {
	"MMMSXXMASM",
	"MSAMXMSMSA",
	"AMXSXMAAMM",
	"MSAMASMSMX",
	"XMASAMXAMM",
	"XXAMMXXAMA",
	"SMSMSASXSS",
	"SAXAMASAAA",
	"MAMMMXMMMM",
	"MXMXAXMASX",
}


var trimmed_sample1 = []string {
	"....XXMAS.",
	".SAMXMS...",
	"...S..A...",
	"..A.A.MS.X",
	"XMASAMX.MM",
	"X.....XA.A",
	"S.S.S.S.SS",
	".A.A.A.A.A",
	"..M.M.M.MM",
	".X.X.XMASX",
}


var trimmed_sample2 = []string {
	".M.S......",
	"..A..MSMS.",
	".M.S.MAA..",
	"..A.ASMSM.",
	".M.S.M....",
	"..........",
	"S.S.S.S.S.",
	".A.A.A.A..",
	"M.M.M.M.M.",
	"..........",
}

func TestPart1(t *testing.T) {
	want := 18

	if got := part1(sample); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart1UsingTrimmedSample(t *testing.T) {
	want := 18

	if got := part1(trimmed_sample1); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart2(t *testing.T) {
	want := 9

	if got := part2(sample); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart2UsingTrimmedSample(t *testing.T) {
	want := 9

	if got := part2(trimmed_sample2); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}
