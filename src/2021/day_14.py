"""Extended Polymerization"""

from collections import defaultdict


if __name__ == '__main__':
    with open('data2.txt') as f:
        template = f.readline().rstrip()
        f.readline()
        pairs = [line.rstrip() for line in f.readlines()]

    rules = {}
    for x in pairs:
        pair, match = x.split(' -> ')
        rules[pair] = match

    freq = defaultdict(lambda: 0)
    for x in template:
        freq[x] += 1

    pairs = defaultdict(lambda: 0)
    for i in range(len(template) - 1):
        pairs[template[i:i + 2]] += 1

    for step in range(40):
        new_pairs = defaultdict(lambda: 0)
        for pair, num in pairs.items():
            insert = rules[pair]
            new_pairs[pair[:1] + insert] += num
            new_pairs[insert + pair[1:]] += num
            freq[insert] += num
        pairs = new_pairs

    high = max(freq.values())
    low = min(freq.values())
    print(high - low)
