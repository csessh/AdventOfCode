package main

import (
	"sort"
	"testing"
)

var sample = []string{
	"47|53",
	"97|13",
	"97|61",
	"97|47",
	"75|29",
	"61|13",
	"75|53",
	"29|13",
	"97|29",
	"53|29",
	"61|53",
	"97|53",
	"61|29",
	"47|13",
	"75|47",
	"97|75",
	"47|61",
	"75|61",
	"47|29",
	"75|13",
	"53|13",
	"",
	"75,47,61,53,29",
	"97,61,53,29,13",
	"75,29,13",
	"75,97,47,61,53",
	"61,13,29",
	"97,13,75,29,47",
}

var rules = map[int][]int{
	47: {53, 61, 13, 29},
	97: {13, 61, 47, 29, 53, 75},
	75: {29, 47, 61, 13, 53},
	61: {13, 53, 29},
	29: {13},
	53: {29, 13},
}

var updates = [][]int{
	{75, 47, 61, 53, 29},
	{97, 61, 53, 29, 13},
	{75, 29, 13},
	{75, 97, 47, 61, 53},
	{61, 13, 29},
	{97, 13, 75, 29, 47},
}

func TestGetMiddleNumber(t *testing.T) {
	test := []int{1, 2, 3}
	want := 2

	if got := getMiddleNumber(test); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}

	test = []int{1, 2, 3, 4, 5}
	want = 3

	if got := getMiddleNumber(test); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestGetMiddleNumberOfEvenLengthSlice(t *testing.T) {
	test := []int{1, 2, 3, 4}

	defer func() {
		if r := recover(); r == nil {
			t.Errorf("The code did not panic, it should have")
		}
	}()

	getMiddleNumber(test)
}

func TestExtraction(t *testing.T) {
	got_rules, got_updates := extractRulesAndUpdates(sample)

	for page, rule := range got_rules {
		sort.Ints(rule)
		sort.Ints(rules[page])

		for i, g := range rule {
			if g != rules[page][i] {
				t.Errorf("got = %v, want %v", g, rules[page][i])
			}
		}
	}

	for i, update := range got_updates {
		sort.Ints(update)
		sort.Ints(updates[i])

		for j, o := range update {
			if o != updates[i][j] {
				t.Errorf("got = %v, want %v", o, updates[i][j])
			}
		}
	}
}

func TestGtComparison(t *testing.T) {
	lhs := 47
	rhs := 53
	want := true

	if got := gt(lhs, rhs, rules); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}

	lhs = 53
	rhs = 47
	want = false

	if got := gt(lhs, rhs, rules); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}

	lhs = 53
	rhs = 53
	want = false

	if got := gt(lhs, rhs, rules); got != want {
		t.Errorf("got = %v, want %v", got, want)
	}
}

func TestTwoParts(t *testing.T) {
	want_good := 143
	want_bad := 123
	r, u := extractRulesAndUpdates(sample)

	if got_good, got_bad := calculate(r, u); got_good != want_good && got_bad != want_bad {
		t.Errorf("got (Part 1 = %v, Part 2 = %v), want (Part 1 = %v, Part 2 = %v)", got_good, want_good, got_bad, want_bad)
	}
}
