package main

import (
	"testing"
)

func TestPingSelf(t *testing.T) {
	var sample = Grid{

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
	want_location := Location{6, 4}
	want_direction := UP
	got_location, got_direction := pingSelf(sample)

	if got_location != want_location {
		t.Errorf("got = %v, want %v", got_location, want_location)
	}

	if got_direction != want_direction {
		t.Errorf("got = %v, want %v", got_direction, want_direction)
	}
}

func TestPart1(t *testing.T) {
	var sample = Grid{
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
	want_steps := 41
	start_location, start_direction := pingSelf(sample)
	_, got_steps := patrol(start_location, start_direction, sample, true)

	if got_steps != want_steps {
		t.Errorf("got = %v, want %v", got_steps, want_steps)
	}
}

func TestPart2(t *testing.T) {
	var sample = Grid{
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
	want_new_blocks := 6
	start_location, start_direction := pingSelf(sample)
	got_new_grids, _ := patrol(start_location, start_direction, sample, true)

	possible_loops := 0
	for _, p := range got_new_grids {
		_, s := patrol(p.loc, p.dir, p.grid, false)
		if s == -1 {
			possible_loops += 1
		}
	}

	if possible_loops != want_new_blocks {
		t.Errorf("got = %v, want %v", possible_loops, want_new_blocks)
	}
}

func TestLoop(t *testing.T) {
	var test = Grid{
		[]byte("....#....."),
		[]byte(".........#"),
		[]byte(".........."),
		[]byte("..#......."),
		[]byte(".......#.."),
		[]byte(".........."),
		[]byte(".#.#^....."),
		[]byte("........#."),
	}

	start_location, start_direction := pingSelf(test)
	_, steps := patrol(start_location, start_direction, test, false)

	if steps != -1 {
		t.Errorf("got = %v, want %v", steps, -1)
	}
}
