from os.path import dirname, join

INPUT_FILE_PATH = join(dirname(dirname(__file__)), "2022/day4_data.txt")

def is_subset(range1: str, range2: str):
  range1 = [int(range1.split('-')[0]), int(range1.split('-')[1])]
  range2 = [int(range2.split('-')[0]), int(range2.split('-')[1])]

  if range1[0] <= range2[0] and range1[1] >= range2[1]:
    return True
  elif range2[0] <= range1[0] and range2[1] >= range1[1]:
    return True
  else:
    return False

def overlap(range1: str, range2: str):
  range1 = [int(range1.split('-')[0]), int(range1.split('-')[1])]
  range2 = [int(range2.split('-')[0]), int(range2.split('-')[1])]

  if range1[0] <= range2[0] and range1[1] >= range2[0]:
    return True
  elif range2[0] <= range1[0] and range2[1] >= range1[0]:
    return True
  else:
    return False


if __name__ == '__main__': 
  with open(INPUT_FILE_PATH) as f:
    assignments = [line.strip().split(',') for line in f.readlines()]

  subsets = [a for a in assignments if is_subset(a[0], a[1])]
  overlaps = [a for a in assignments if overlap(a[0], a[1])]

  print(f"Part 1: {len(subsets)}")
  print(f"Part 2: {len(overlaps)}")
    