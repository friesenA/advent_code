def part1(elves_calories):
  
  result = max(elves_calories)

  print(f'highest_calories: {result}')

def part2(elves_calories):
  top3 = []
  for x in range(3):
    top = max(elves_calories)
    top3.append(top)
    index = elves_calories.index(top)
    elves_calories.pop(index)
  
  print(f'top three calories: {sum(top3)}')
    

if __name__ == "__main__":
  with open("src/2022/day1_data.txt") as f:
    data_points = [e.replace('\n', '') for e in f.readlines()]

  elves = []
  elf = []
  for data in data_points: 
    if data:
      elf.append(int(data))
    else:
      elves.append(elf.copy())
      elf = []

  elves_calories = [sum(a) for a in elves]

  part1(elves_calories)
  part2(elves_calories)