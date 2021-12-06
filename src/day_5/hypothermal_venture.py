"""Hypothermal venture"""

class Point:
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __repr__(self):
    return f'({self.x},{self.y})'

    
class Line:
  
  def __init__(self, p1, p2):
    if p1.x == p2.x:
      start, end = min(p1.y, p2.y), max(p1.y, p2.y)
      self.points = [Point(p1.x, y) for y in range(start, end + 1)]
    elif p1.y == p2.y:
      start, end = min(p1.x, p2.x), max(p1.x, p2.x)
      self.points = [Point(x, p1.y) for x in range(start, end + 1)]
    else:
      self.points = []
      x_diff = p1.x - p2.x
      y_diff = p1.y - p2.y
      x_sign = -1 if x_diff > 0 else 1
      y_sign = -1 if y_diff > 0 else 1
      for i in range(abs(x_diff) + 1):
        self.points.append(Point(p1.x + i * x_sign, p1.y + i * y_sign))
      
  def __repr__(self):
    return str(self.points)
      
    
if __name__ == '__main__':
  with open('data.txt') as f:
     lines = f.readlines()
  
  vent_lines = []
  max_x, max_y = 0, 0
  for line in lines:
    start, end = line.rstrip().split(' -> ')
    start, end = Point(*map(int, start.split(','))), Point(*map(int, end.split(',')))
    vent_lines.append(Line(start, end))
    
    max_x = max(max_x, start.x, end.x)
    max_y = max(max_y, start.y, end.y)
    
  print(f'Grid is: {max_x}x{max_y}')
      
  graph = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
  for line in vent_lines:
    for point in line.points:
      graph[point.y][point.x] += 1
  
  count = sum([sum([1 for x in y if x > 1]) for y in graph])
          
  print(count)
     
