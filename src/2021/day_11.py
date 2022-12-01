"""Dumbo Octopus"""

def flash(r, c, grid, width, length):
    grid[r][c] = 0
    if r - 1 in width:
        grid[r - 1][c] += 1
        if c - 1 in length:
            grid[r - 1][c - 1] += 1
        if c + 1 in length:
            grid[r - 1][c + 1] += 1

    if r + 1 in width:
        grid[r + 1][c] += 1
        if c - 1 in length:
            grid[r + 1][c - 1] += 1
        if c + 1 in length:
            grid[r + 1][c + 1] += 1

    if c - 1 in length:
        grid[r][c - 1] += 1

    if c + 1 in length:
        grid[r][c + 1] += 1


def grid_repr(grid):
    string = '\n'
    for row in grid:
        string += ' '.join(map(str, row)) + '\n'

    return string


if __name__ == '__main__':
    with open('data2.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]
        grid = [[int(x) for x in row] for row in lines]

    width = len(grid[0])
    length = len(grid)

    num_flashes = 0
    for step in range(500):
        changes = True
        grid = [[x + 1 for x in row] for row in grid]
        flashes = []
        while changes:
            changes = False
            for r, row in enumerate(grid):
                for c, col in enumerate(row):
                    if col >= 10:
                        changes = True
                        flashes.append((r, c))
                        flash(r, c, grid, range(width), range(length))

            for r, c in flashes:
                grid[r][c] = 0

        if len(flashes) == width * length:
            print(f'Step {step + 1} all flash')
            print(grid_repr(grid))
            break

        num_flashes += len(flashes)

        print(f'Step {step + 1}:')
        print(grid_repr(grid))

    print(f'\nFlashes = {num_flashes}')
