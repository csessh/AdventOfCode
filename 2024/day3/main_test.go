package main

import (
	"testing"
)

func TestPart1(t *testing.T) {
	var samples = []string{
		"xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))",
	}
	want := 161

	if got := part1(samples); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart2(t *testing.T) {
	var samples = []string{
		"xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))",
	}
	want := 48

	if got := part2(samples); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestPart2WithCustomTestCases(t *testing.T) {
	var samples = []string{
		"don't()-xmul(2,4)&mul[3,7]!^_mul(5,5)+mul(32,64](mul(11,8)un-do()?mul(8,5))",             // 40
		"don't()-xmul(2,4)&-don't()-mul[3,7]!^_mul(5,5)+mul(32,64](mul(11,8)un-do()?mul(8,5))",    // 40
		"mul(1,1)don't()mul(1,1)mul(1,1)mul(1,1)mul(1,1)do()mul(1,1)mul(1,1)",                     // 3
		"mul(1,1)don't()mul(1,1)mul(1,1)mul(1,1)mul(1,1)do()mul(1,1)mul(1,1)do()mul(1,1)mul(1,1)", // 5
		"mul(1,1)don't()do()mul(1,1)", // 2
		"mul(1,2)do()don't()mul(1,1)", // 2
	}

	var wants = []int{40, 40, 3, 5, 2, 2}

	for i, sample := range samples {
		input := []string{sample}
		if got := part2(input); got != wants[i] {
			t.Errorf("got = %v, want %v", got, wants[i])
		}
	}
}

func TestPart2ConsiderWholeFileAsOneLongMemory(t *testing.T) {
	var samples = []string{
		"mul(1,1)don't()mul(1,1)",
		"mul(1,2)do()mul(1,1)",
	}

	want := 2

	if got := part2(samples); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}
