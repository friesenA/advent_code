"""Passage Pathing"""
from collections import defaultdict


def find_paths(graph, start, visited, sc, path, paths):

    if not start.isupper():
        visited[start] = True
    path.append(start)

    if start == 'end':
        paths.append(path.copy())
    else:
        for i in graph[start]:
            if visited[i] == False:
                find_paths(graph, i, visited, sc, path, paths)
            elif sc is None and i not in ['start', 'end']:
                find_paths(graph, i, visited, i, path, paths)

    path.pop()
    if start != sc:
        visited[start] = False
    return paths


if __name__ == '__main__':
    with open('data4.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    graph = defaultdict(list)

    for line in lines:
        a, b = line.split('-')
        graph[a].append(b)
        graph[b].append(a)

    print(graph)
    paths = find_paths(graph, 'start', defaultdict(lambda: False), None, [], [])
    print(paths)
    print(len(paths))
