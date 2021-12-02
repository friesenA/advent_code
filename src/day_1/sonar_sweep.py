"""Sonar Sweep"""

def part1(data_points):
  count = 0
  for i, value in enumerate(data_points):
    if i == 0:
      continue
    if value > data_points[i-1]:
      count += 1
     
  return count


def part2(filename):
  count = 0
  for i, calue in enumerate(data_points):
    if i == 0 or i + 3 > len(data_points):
      continue
    if window(data_points, range(i, i+3)) > window(data_points, range(i-1, i+2)):
      count += 1
  
  return count
      
def window(data_points, range):
  total = 0
  for i in range:
    total += data_points[i]
    
  return total
  

if __name__ == '__main__':
  with open('data.txt') as f:
    data_points = [int(e.replace('\n', '')) for e in f.readlines()]

  print(f'part 1: {part1(data_points)}')
  print(f'part 2: {part2(data_points)}')
