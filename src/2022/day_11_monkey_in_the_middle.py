from math import floor
import re

class Monkey:

  def __init__(self, items, operation, dividend, throw) -> None:
    self.items = items
    self.operation = operation
    self.dividend = dividend
    self.throw = throw
    self.counter = 0

  def from_parse(starting_items, operation, test, result_true, result_false) -> "Monkey":
    items = [int(x) for x in re.search(r'Starting items: (.+)', starting_items).group(1).split(", ")]
    op = re.search(r"Operation: new = (.+)", operation).group(1)
    dividend = int(re.search(r"Test: divisible by (.+)", test).group(1))
    throw = {
      True: int(re.search(r"throw to monkey (.+)", result_true).group(1)),
      False: int(re.search(r"throw to monkey (.+)", result_false).group(1))
    }
    return Monkey(items, op, dividend, throw)

  def inspect(self) -> int:
    self.counter += 1
    item = self.items.pop(0)
    item = self.execute_operation(item)
    # item = int(floor(item/3))

    test = floor(item/self.dividend) == item/self.dividend
    return item, self.throw[test]

  def execute_operation(self, old) -> int:
    return(eval(self.operation))
    
def monkey_business(monkeys) -> int:
  counts = [monkey.counter for monkey in monkeys]
  active1 = max(counts)
  counts.remove(active1)
  active2 = max(counts)
  return active1 * active2

if __name__ == '__main__':
  with open('src/2022/day11_data.txt') as f:
    dataset = [line.rstrip() for line in f.readlines()]

  monkeys = [Monkey.from_parse(*dataset[x+1:x+6]) for x in range(0, len(dataset), 7)] 

  for i in range(10000):
    for monkey in monkeys:
      for x in range(len(monkey.items)):
        item, destination = monkey.inspect()
        monkeys[destination].items.append(item)


  print(f"Part 1: {monkey_business(monkeys)}")