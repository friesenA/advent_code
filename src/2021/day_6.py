"""Lanternfish"""

from itertools import groupby


def calculation(ages):
    ages = [int(x) for x in ages]
    ages.sort()

    groups = {i: 0 for i in range(9)}
    for age, grp in groupby(ages):
        groups[age] = len(list(grp))

    for _ in range(256):
        new = groups[0]
        groups = {key: groups[key + 1] for key in groups.keys() if key != 8}
        groups[8] = new
        groups[6] += new

    return sum(groups.values())


if __name__ == '__main__':
    with open('data.txt') as f:
        line = f.readline().rstrip().split(',')

    fish = calculation(line)

    print(fish)
