# [Advent of Code](https://adventofcode.com/)

[2021](/2021/) was me learning Ruby. [2022](/2022/) is me getting back into Python.

## Notes

- Python naming conventions
  - https://github.com/naming-convention/naming-convention-guides/tree/master/python (based on
  Guido's conventions)
  - https://softwareengineering.stackexchange.com/a/399583/50096
  - https://stackoverflow.com/a/48721872/575530 (variables)

## TODO

- [x] Write unit tests
  - [x] For utility functions
  - [x] For the main functionality in parts 1 and 2
  - [x] Add coverage (run as, for example, `coverage run -m pytest 2022/test_day10.py`)
- [x] Git
  - [x] Move input data to private sub-repo
  - [x] Combine years into one repo
- [ ] Have these examples and answers served by Django, VueJS, and SVG
- [ ] Dockerize
- [ ] Use a cloud VM rather than local
- [ ] Make maximum use of
  - [ ] Functional programming style built in list etc. handling (e.g. `map`)
  - [ ] NumPy
  - [ ] Pandas

## Reflections

### Day 1

- Careful about the end of inputs, does the final `add` get triggered correctly
- Pandas `nlargest` was useful and [more performant](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html#pandas.DataFrame.nlargest) than sorting.
- Make sure the debugger is working

### Day 3

- `@classmethod` is handy to make things testable
- Use `pytest` and write simple unit tests as I go along so I have confidence about the utility methods

### Day 4

- Other code niceties are `_private_methods` (a convention) `@property` and `from functools import cached_property`
- Good tests really sped this up, but

### Day 5

- Edge conditions not present in test data floored me repeatedly. When I refactor it's important that tests catch new errors
- Are regexes simpler/better than raw indexes?
- `[::-1]` looked cryptic, but is just the `[start:stop:step]` and reverses the list
- I needn't have kept the crate's `[` & `]`, that caused trouble printing
- A mixture of proper debugging and printing was useful, would a _to string_ function have been used in the debugger's output?

### Day 7

- Use `dirs = [] + self._sub_dirs` to avoid taking a second pointer to `self._sub_dirs`.
- I can use `if file_match := re.match('(\d+) (.*)', row)` instead of `file_match = re.match('(\d+) (.*', row)` then `if file_match:`.
- There are two edge cases that don't get exercised by the test data nor the real data. Almost everybody's solution fails the first one (mine included) and most fail the second. Should I be
basing things on the data more than the question itself?
  - `$ cd /` should take you back to the root from wherever you currently are
  - Revisiting and `ls` in the same directory twice should not double its size!

### Day 9

- Careful reading, e.g. H, 1, … 9 is 10 knots, not 9.

### Day 10

- 100% coverage is satisfying
- Part 2 was not accessible for visually impaired programmers
- We should **not** be committing input files ([reddit thread](https://www.reddit.com/r/adventofcode/comments/zh2hk0/2022friendly_reminder_dont_commit_your_input/)). That'll be a good excuse to look at sub-repositories
  - Took the opportunity to combine my 2021 and 2022 repositories (following [this SO answer](https://stackoverflow.com/a/10548919/575530) using the [allow-unrelated-histories](https://git-scm.com/docs/git-merge#Documentation/git-merge.txt---allow-unrelated-histories)).
  - Used git's [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules#_starting_submodules) feature to move all the copied AoC inputs (test and real) to a private repository.
- Calling `Monkey.bored_with` picks the instance method not the class method of the same name!

### Day 11

- Part 2 was hard. The breakthrough for me was `throw['item'] %= self.product` which was a result of
me realising it was mathematical (from a comment on reddit).

### Day 12

- Remember in `or` to negate first when tacking second if needed
- Passing logic tests and functions (e.g. `stop_test` and `neighbours_func`) would have made
refactoring straightforward, but may have been premature complexity. Anyway it was easy to fix.
- If Eric had not made the Part 2 data take soooo long on the naive solution I would never have
fixed it!

### Day 13

- Writing `logging.info` statements to reproduce Eric's explanatory test is a useful additional test
if the algorithm passes on the test data but fails on the 'real' data (see [reddit thread](https://old.reddit.com/r/adventofcode/comments/zkq7qk/2022_day_13_part_1_debugging_advice_please/))
- Lots of my time is wasted with sloppy writing, e.g. `[i for i in range(self.sorted_packets) if self.sorted_packets[i] in self.divider_packets.contains]` instead of `[i + 1 for i in range(len(self.sorted_packets)) if self.sorted_packets[i] in self.divider_packets]`

### Day 14

- `extend` instead of `append` adds the items in the list. No need to worry about how to flatten.
- To use the `capfd` fixture pass it into the test function, then call `out, _ = capfd.readouterr()`
to get `stdout` _after_ the `print` statements.

### Day 15

- Note to self — do *not* forget to uses square brackets for `loc` and `iloc` in pandas, i.e.
`self.grid.loc[y].value_counts()['#']` not `self.grid.loc(y).value_counts()['#']`
- Cute way using double comprehension to get all pairs `[(s1, s2) for i, s1 in enumerate(self.sensors) for s2 in self.sensors[i + 1:]]`
- I should have taken a geometric approach to the algorithms from the start. I may need to be more on
top of geometric algorithms for SVG work anyway. Some interesting solutions at:
  - [jakesco Part 1](https://github.com/jakesco/AOC2022/blob/main/aoc/solutions/day15.py) (GitHub)
  - [JakubDotPy Part 2](https://github.com/JakubDotPy/aoc2022/blob/master/day15/part2.py) (GitHub)
  - [RGodlike Comparison of different approaches](https://old.reddit.com/r/adventofcode/comments/zml8ee/2022_day_15_part_2_comparison_of_different/) (Reddit)
  - [appus3r Can't think of an approach](https://old.reddit.com/r/adventofcode/comments/zmjcgl/2022_day_15_part_2_python_cant_think_of_an/) (Reddit)
  - [Ayman4Eyes No search formula](https://old.reddit.com/r/adventofcode/comments/zmjzu7/2022_day_15_part_2_no_search_formula/) (reddit)
  - [Day 15 Solutions Megathread](https://old.reddit.com/r/adventofcode/comments/zmcn64/2022_day_15_solutions/) (reddit)
    - [codertee](https://github.com/codertee/adventofcode/blob/af3563f8993b7cad46d1f674bf8d192cd4361ff8/adventofcode/solutions/y2022/d15.py) (Github)
    - [olliemath](https://github.com/olliemath/AdventOfCode/blob/master/2022/day_15/solution.py) rotates the coords to get squares (Github)
    - [msschmitt](https://old.reddit.com/r/adventofcode/comments/zmcn64/2022_day_15_solutions/j0ed813/) merging ranges (Reddit)
    - [zniperr](https://old.reddit.com/r/adventofcode/comments/zmcn64/2022_day_15_solutions/j0dvz1y/) border checking code (Reddit)

### Day 16

- [mebeim's solutions](https://github.com/mebeim/aoc/tree/master/2022) are very useful since he
includes a walkthrough of the code and his thinking