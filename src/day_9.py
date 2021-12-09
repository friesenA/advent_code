"""Smoke Basin"""


def low_points(heightmap, width, length):
    sum = 0
    points = []
    for i, row in enumerate(heightmap):
        for j, col in enumerate(row):
            if j - 1 in width and heightmap[i][j] >= heightmap[i][j - 1]:
                continue
            if i - 1 in length and heightmap[i][j] >= heightmap[i - 1][j]:
                continue
            if j + 1 in width and heightmap[i][j] >= heightmap[i][j + 1]:
                continue
            if i + 1 in length and heightmap[i][j] >= heightmap[i + 1][j]:
                continue

            print(f"Local minimum at {i},{j} with value {heightmap[i][j]}")
            points.append((i, j))
            sum += int(heightmap[i][j]) + 1

    print(f"Low point sum: {sum}")
    return points


def basin_size(point, heightmap, width, length):
    basin = {point}
    points = {point}
    while points:
        new = set()
        for i, j in points:
            if j - 1 in width and int(heightmap[i][j - 1]) < 9:
                new.add((i, j-1))
            if i - 1 in length and int(heightmap[i - 1][j]) < 9:
                new.add((i - 1, j))
            if j + 1 in width and int(heightmap[i][j + 1]) < 9:
                new.add((i, j + 1))
            if i + 1 in length and int(heightmap[i + 1][j]) < 9:
                new.add((i + 1, j))

        points = (new - basin)
        basin.update(points)

    return len(basin)


if __name__ == '__main__':
    with open('data2.txt') as f:
        lines = f.readlines()
        heightmap = [line.rstrip() for line in lines]

    width = range(0, len(heightmap[0]))
    length = range(0, len(heightmap))

    print(f"Map of {width} x {length}")

    points = low_points(heightmap, width, length)

    basins = []
    for point in points:
        size = basin_size(point, heightmap, width, length)
        basins.append(size)

    basins.sort(reverse=True)
    print(f"Basins: {basins[0]}, {basins[1]}, {basins[2]}")
    print(f"Result: {basins[0] * basins[1] * basins[2]}")
