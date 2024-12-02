package main

import (
	"testing"
	"strings"
)

var sample = `7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9`

var reports = strings.Split(sample, "\n")
var bad_reports = [4]string{
	"1 2 7 8 9",
	"9 7 6 2 1",
	"1 3 2 4 5",
	"8 6 4 4 1",
}

func TestPart1(t *testing.T) {
	want_count := 2
	got_count, got_bad_reports := part1(reports)

	if got_count != want_count {
		t.Errorf("got = %v, want %v", got_count, want_count)
	}

	if len(got_bad_reports) != len(bad_reports) {
		t.Errorf("got %d bad reports, want %d", len(got_bad_reports), len(bad_reports))
	}

	for i, report := range got_bad_reports {
		if report != bad_reports[i] {
			t.Errorf("got %s, want %s", report, bad_reports[i])
		}
	}
}

func TestPart2(t *testing.T) {
	want := 2 

	if got := part2(bad_reports[:]); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}
