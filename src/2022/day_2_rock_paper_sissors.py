import enum

win_points = 6
draw_points = 3

####### Part 1 ##########
class attack(enum.Enum):
  R = 1
  P = 2
  S = 3

  def __lt__(self, other):
    if self.__class__ is other.__class__:
      if other.value - self.value == 1 or self.value - other.value == 1:
        return self.value < other.value
      else:
        return self.value > other.value
    return NotImplemented

code = {
  "A": attack.R,
  "B": attack.P,
  "C": attack.S,
  "X": attack.R,
  "Y": attack.P,
  "Z": attack.S,
}

def match(them, you):
  if code[them] == code[you]:
    return code[you].value + draw_points
  if code[you] > code[them]:
    return code[you].value + win_points
  else: # lose
    return code[you].value

####### Part 2 ##########

def match2(them, outcome):
  if outcome == "Y": # draw
    return code[them].value + draw_points
  if outcome == "X": # lose
    value = code[them].value - 1
    return value if value != 0 else 3
  if outcome == "Z": # win
    value = code[them].value + 1
    value = value if value != 4 else 1
    return value + win_points


if __name__ == "__main__":
  with open("src/2022/day2_data.txt") as f:
    data_points = [line.replace('\n', '').split(' ') for line in f.readlines()]

  print(f"Part 1: {sum([match(e[0], e[1]) for e in data_points])}")
  print(f"Part 1: {sum([match2(e[0], e[1]) for e in data_points])}")

