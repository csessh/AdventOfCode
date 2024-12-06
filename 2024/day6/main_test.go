package main

import (
	"testing"
)

var sample = [][]byte{
	[]byte("....#....."),
	[]byte(".........#"),
	[]byte(".........."),
	[]byte("..#......."),
	[]byte(".......#.."),
	[]byte(".........."),
	[]byte(".#..^....."),
	[]byte("........#."),
	[]byte("#........."),
	[]byte("......#..."),
}

func TestPart1(t *testing.T) {
	want_steps := 41
	want_blockages := 6
	got_steps, got_blockages := part1(sample)

	if got_steps != want_steps {
		t.Errorf("got = %v, want %v", got_steps, want_blockages)
	}

	if got_blockages != want_blockages {
		t.Errorf("got = %v, want %v", got_blockages, want_blockages)
	}
}

