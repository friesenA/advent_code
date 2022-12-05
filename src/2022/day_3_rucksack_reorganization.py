from collections import defaultdict 

capital_offset = 65
lowercase_offset = 97
problem_capital_offset = 27
problem_lowercase_offset = 1

def calculate_value(char):
  if char.islower():
    return problem_lowercase_offset + ord(char) - lowercase_offset
  else:
    return problem_capital_offset + ord(char) - capital_offset

######### Part 1 ###############
def find_error(compartment1, compartment2):
  items = {item:"present" for item in compartment1}
  for item in compartment2:
    if items.get(item) != None:
      return item
  raise Exception('No item found')

######### Part 2 ###############
def find_badge(bags):
  items = defaultdict(lambda: dict())
  for id, bag in enumerate(bags):
    for item in bag:
      items[item][id] = "present"
  for item, ids in items.items():
    if len(ids.keys()) == 3:
      return item


if __name__ == '__main__':
  with open('src/2022/day3_data.txt') as f:
    rucksacks = [line.replace('\n', '') for line in f.readlines()]
    
  
  rucksack_compartments = [(r[:int(len(r)/2)], r[int(len(r)/2):]) for r in rucksacks]
  errors = [find_error(items1, items2) for items1, items2 in rucksack_compartments]

  badges = []
  n = 0
  while n < len(rucksacks):
    badges.append(find_badge([rucksacks[n], rucksacks[n+1], rucksacks[n+2]]))
    n += 3

  print(badges)
  print(f'Part 1: {sum([calculate_value(e) for e in errors])}')
  print(f'Part 2: {sum([calculate_value(b) for b in badges])}')