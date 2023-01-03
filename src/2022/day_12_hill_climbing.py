
def print_graph(graph):
  for row in graph:
    print(row)


def find_character(graph, char):
  for y, row in enumerate(graph):
    if row.find(char) != -1:
      return (row.find(char), y)

def find_characters(graph, char):
  instances = []
  for y, row in enumerate(graph):
    if row.find(char) != -1:
      instances.append((row.find(char), y))
  return instances

def generate_cost_graph_v2(graph, start, end):
  evaluating_nodes = {start: 0}
  completed_nodes = [[False for x in row] for row in dataset]
  cost_graph[start[1]][start[0]] = 0

  node = start
  while(len(evaluating_nodes.keys()) != 0 and node != end):
    evaluating_nodes.pop(node, None)
    x, y = node
    completed_nodes[y][x] = True

    current_cost = cost_graph[y][x]
    # print(node)
    if x > 0 and completed_nodes[y][x-1] == False and ord(graph[y][x-1]) - ord(graph[y][x]) <= 1:
      cost = min(cost_graph[y][x-1], current_cost + 1)
      evaluating_nodes[(x-1, y)] = cost
      cost_graph[y][x-1] = cost
    if y > 0 and completed_nodes[y-1][x] == False and ord(graph[y-1][x]) - ord(graph[y][x]) <= 1:
      cost = min(cost_graph[y-1][x], current_cost + 1)
      evaluating_nodes[(x, y-1)] = cost
      cost_graph[y-1][x] = cost
    if x < len(graph[y]) - 1 and completed_nodes[y][x+1] == False and ord(graph[y][x+1]) - ord(graph[y][x]) <= 1:
      cost = min(cost_graph[y][x+1], current_cost + 1)
      evaluating_nodes[(x+1, y)] = cost
      cost_graph[y][x+1] = cost
    if y < len(graph) - 1 and completed_nodes[y+1][x] == False and ord(graph[y+1][x]) - ord(graph[y][x]) <= 1:
      cost = min(cost_graph[y+1][x], current_cost + 1)
      evaluating_nodes[(x, y+1)] = cost
      cost_graph[y+1][x] = cost

    node = min(evaluating_nodes, key=evaluating_nodes.get)

  return cost_graph

if __name__ == '__main__':
  with open('src/2022/day12_data.txt') as f:
    dataset = [line.rstrip() for line in f.readlines()]

  cost_graph = [[10000 for x in row] for row in dataset]
  start = find_character(dataset, "S")
  end = find_character(dataset, "E")
  graph = [row.replace("S", "a").replace("E", "z") for row in dataset]
  print(f"start: {start}, end: {end}")

  cost_graph = generate_cost_graph_v2(graph, start, end)
  print(f"Part 1: {cost_graph[end[1]][end[0]]}")

  low_nodes = find_characters(graph, "a")
  print(f"Part 2: {min([generate_cost_graph_v2(graph, a, end)[end[1]][end[0]] for a in low_nodes])}")
  
