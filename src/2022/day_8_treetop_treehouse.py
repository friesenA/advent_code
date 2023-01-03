def find_visible_trees(graph):
  visibility = [[0 for char in line] for line in graph]
  for x in range(len(graph)):
    for y in range(len(graph[0])):
      # print(f'x={x}, y={y}')
      if x == 0 or y == 0 or x == len(graph) - 1 or y == len(graph[0]) - 1:
        visibility[x][y] = 1
      # up
      elif all(graph[x][y] > z[y] for z in graph[:x]):
        visibility[x][y] = 1
      # down
      elif all(graph[x][y] > z[y] for z in graph[x + 1:]):
        visibility[x][y] = 1
      # left
      elif all(graph[x][y] > z for z in graph[x][:y]):
        visibility[x][y] = 1
      # right
      elif all(graph[x][y] > z for z in graph[x][y + 1:]):
        visibility[x][y] = 1
      else: 
        visibility[x][y] = 0
      # print(visibility)

  return visibility

def find_scenic_score(graph):
  scores = [[1 for char in line] for line in graph]
  for x, row in enumerate(graph):
    for y, column in enumerate(row):
      # print(f'x={x}, y={y}')
      # up
      trees = find_num_visible(column, [x for x in reversed([z[y] for z in graph[:x]])])
      scores[x][y] *= trees
      # down
      trees = find_num_visible(column, [z[y] for z in graph[x + 1:]])
      scores[x][y] *= trees
      # left
      trees = find_num_visible(column, [x for x in reversed([z for z in graph[x][:y]])])
      scores[x][y] *= trees
      # right
      trees = find_num_visible(column, [z for z in graph[x][y + 1:]])
      scores[x][y] *= trees
      # print(scores)
  return scores

def find_num_visible(house: int, trees):
  sum = 0
  for tree in trees:
    if house > tree:
      sum +=1
    else:
      break
  if sum < len(trees):
    sum += 1
  return sum


if __name__ == '__main__':
  with open('src/2022/day8_data.txt') as f:
    dataset = [line.replace('\n', '') for line in f.readlines()]

  visible_trees = find_visible_trees(dataset)
  print(f"Part 1: {sum([sum(row) for row in visible_trees])}")
  scores = find_scenic_score(dataset)
  print(f"Part 2: {max([max(row) for row in scores])}")