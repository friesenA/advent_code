"""Extended Polymerization"""


class Point(tuple):

    def __new__(self, x, y):
        return tuple.__new__(Point, (x, y))

    def above(self):
        return Point(self[0] - 1, self[1])

    def below(self):
        return Point(self[0] + 1, self[1])

    def before(self):
        return Point(self[0], self[1] - 1)

    def after(self):
        return Point(self[0], self[1] + 1)


class Map:

    def __init__(self, array):
        self.array = array
        self.width = len(array[0])
        self.length = len(array)

    def get(self, point):
        return self.array[point[0]][point[1]]

    def set(self, point, value):
        self.array[point[0]][point[1]] = value

    def __contains__(self, point):
        return point[0] in range(width) and point[1] in range(length)

    def __repr__(self):
        return '\n'.join(['  '.join([str(self.array[i][j]) for j in range(width)]) for i in range(length)])


def shortest_path(array, start, end):
    unvisited = {}
    for x in range(width):
        for y in range(length):
            unvisited[Point(x, y)] = None
    partial = {start: array.get(start)}

    position = start
    while position != end:
        unvisited.pop(position)
        current_cost = partial.pop(position)
        for adjacent in ['above', 'below', 'before', 'after']:
            adj_node = getattr(position, adjacent)()
            if adj_node in array and adj_node in unvisited:
                cost = current_cost + array.get(adj_node)
                if not partial.get(adj_node) or cost < partial[adj_node]:
                    partial[adj_node] = cost

        minimum = min(partial.values())
        position = [key for key, value in partial.items() if value == minimum][0]

    return partial[end] - array.get(start)


if __name__ == '__main__':
    with open('data2.txt') as f:
        array = [[int(x) for x in line.rstrip()] for line in f.readlines()]

    grids = {}

    master_array = []
    for row_duplicate in range(5):
        for row in array:
            row_array = []
            for col_duplicate in range(5):
                multiplier = row_duplicate + col_duplicate
                row_array.extend([x + multiplier if x + multiplier < 10 else ((x + multiplier) % 10) + 1 for x in row])
            master_array.append(row_array)

    width = len(master_array[0])
    length = len(master_array)

    print(f'Array dimensions {(width, length)}')

    print(Map(master_array))
    print('')

    result = shortest_path(Map(master_array), Point(0, 0), Point(width - 1, length - 1))
    print(f'Shortest path: {result}')
