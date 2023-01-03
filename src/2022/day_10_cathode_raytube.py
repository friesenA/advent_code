def add_to_x(line):
  if "addx" in line:
    add = int(line.split(" ")[1])
  else:
    add = 0
  return add

def render_cpu_register(dataset):
  register_over_time = [1]
  x = 1

  for line in dataset:
    if "noop" in line:
      register_over_time.append(x)
    elif "addx" in line:
      register_over_time.append(x)
      x += add_to_x(line)
      register_over_time.append(x)
      
  return register_over_time


def determine_signal_strengths(register):
  measure_points = [20, 60, 100, 140, 180, 220]

  signal_strengths = [value * (i + 1) for i, value in enumerate(register) if i + 1 in measure_points]
  
  return signal_strengths


def render_crt(register):
  crt = [["." for x in range(40)] for y in range(6)]
  for x in range(40):
    for y in range(6):
      cycle = y * 40 + x
      if abs(register[cycle] - x) <= 1:
        crt[y][x] = "#"

  return crt

def draw(array):
  for row in array:
    print("".join(row))


if __name__ == '__main__':
  with open('src/2022/day10_data.txt') as f:
    dataset = [line.replace('\n', '') for line in f.readlines()]

  register = render_cpu_register(dataset)
  print(f"Part 1: {sum(determine_signal_strengths(register))}")
  print(f"Part 2: ")
  draw(render_crt(register))
