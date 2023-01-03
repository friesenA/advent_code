# import re
# from collections import defaultdict

# if __name__ == '__main__': 
#   with open('src/2022/day5_data.txt') as f:
#     dataset = [line for line in f.readlines()]

#   moves = [line.strip() for line in dataset if line.startswith("move")]
#   moves = [[groups for groups in re.match(r"move (\d+) from (\d+) to (\d+)", move).groups()] for move in moves]
#   print(moves)

#   size = 3
#   grid = defaultdict(lambda: list())
#   for line in dataset:
#     if line[1] == "1":
#       break
#     for x in range(size):
#       if line[4 * x + 1] != " ":
#         grid[(x+1)].append(line[4 * x + 1])

#   print(grid)

import re

s = []

x = open('src/2022/day5_data.txt')

for line in x:
    if line == "\n": break
    s.append([line[k * 4 + 1] for k in range(len(line) // 4)]) # this is just line[1::4] - thanks UnrelatedString

s.pop()
s = [list("".join(c).strip()[::-1]) for c in zip(*s)]

for line in x:
    a, b, c = map(int, re.findall("\\d+", line))
    s[c - 1].extend(s[b - 1][-a:][::-1])
    s[b - 1] = s[b - 1][:-a]

print("".join([a[-1] for a in s]))