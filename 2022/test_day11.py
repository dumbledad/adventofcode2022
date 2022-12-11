from day11 import Troupe, Monkey

def test_troupe_init():
  troupe = Troupe('inputs/2022/day11-test.txt')
  assert troupe.data
  assert len(troupe.monkeys) == 4
  assert troupe.monkeys[3].items == [74]
  assert troupe.monkeys[2].operation == 'new = old * old'
  assert troupe.monkeys[1].test['divisor'] == 19
  assert troupe.monkeys[0].test['true'] == 2
  assert troupe.monkeys[0].test['false'] == 3

def test_monkey_inspect():
  troupe = Troupe('inputs/2022/day11-test.txt')
  assert troupe.monkeys[0].inspect(10) == 190

def test_monkey_throw_to():
  troupe = Troupe('inputs/2022/day11-test.txt')
  assert troupe.monkeys[2].throw_to(26) == 1
  assert troupe.monkeys[2].throw_to(27) == 3

def test_troupe_perform_round():
  troupe = Troupe('inputs/2022/day11-test.txt')
  troupe.perform_round()
  assert troupe.monkeys[0].items == [20, 23, 27, 26]
  assert troupe.monkeys[1].items == [2080, 25, 167, 207, 401, 1046]
  assert troupe.monkeys[2].items == []
  assert troupe.monkeys[3].items == []

def test_troupe_inspection_count():
  troupe = Troupe('inputs/2022/day11-test.txt')
  troupe.perform_rounds(20)
  assert troupe.monkeys[0].inspection_count == 101
  assert troupe.monkeys[1].inspection_count == 95
  assert troupe.monkeys[2].inspection_count == 7
  assert troupe.monkeys[3].inspection_count == 105

def test_troupe_monkey_business():
  troupe = Troupe('inputs/2022/day11-test.txt')
  troupe.perform_rounds(20)
  assert troupe.monkey_business == 10_605
