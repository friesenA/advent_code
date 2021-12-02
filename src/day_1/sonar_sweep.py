"""Sonar Sweep"

if __name__ == '__main__':
  with open('data.txt') as f:
    data_points = f.readlines()

  count = 0
  for i, value in enumerate(data_points):
    if i = 0:
      continue
    if value > dat_points[i-1]:
      count += 1
  
  print(count)
