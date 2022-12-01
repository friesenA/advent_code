"""Transparent Origami"""

def fold_paper(dots, instruction):
    dir, value = instruction.split('=')
    value = int(value)
    index = 0 if dir == 'x' else 1

    after_fold = set()
    for dot in dots:
        if dot[index] < value:
            after_fold.add(dot)
        else:
            change = list(dot)
            change[index] = value - (dot[index] - value)
            after_fold.add(tuple(change))

    return after_fold


def find_size(dots):
    width = max([x[0] for x in dots]) + 1
    length = max([x[1] for x in dots]) + 1

    return width, length


if __name__ == '__main__':
    dots = set()
    instructions = []
    with open('data2.txt') as f:
        line = f.readline()
        while line != '\n':
            x, y = line.rstrip().split(',')
            dots.add((int(x), int(y)))
            line = f.readline()

        for line in f.readlines():
            _, _, x = line.rstrip().split(' ')
            instructions.append(x)

    print(dots)
    print(instructions)

    width, length = find_size(dots)

    print(f'Paper is {width}x{length}')

    for instruction in instructions:
        dots = fold_paper(dots, instruction)

    width, length = find_size(dots)
    print(f'Paper is {width}x{length}')

    for y in range(length):
        str = ''
        for x in range(width):
            for dot in dots:
                if dot == (x, y):
                    str += '#'
                    break
            else:
                str += '.'
        print(str)
