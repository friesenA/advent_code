"""Syntax Scoring"""


CORRUPTION_SCORE = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
COMPLETION_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
BRACKETS = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
REVERSE_BRACKETS = {v: k for k, v in BRACKETS.items()}
OPEN = BRACKETS.keys()
CLOSE = BRACKETS.values()


def score_errors(corrupted):
    return sum([CORRUPTION_SCORE[item] for item in corrupted])


def score_completion(completions):
    scores = []
    for completion in completions:
        print(completion)
        score = 0
        for symbol in completion:
            score *= 5
            score += COMPLETION_SCORE[symbol]
        scores.append(score)

    scores.sort()
    return scores[int((len(scores) - 1)/2)]


if __name__ == '__main__':
    with open('data2.txt') as f:
        lines = [line.rstrip() for line in f.readlines()]

    corrupted = []
    completions = []
    for line in lines:
        stack = []
        for symbol in line:
            if symbol in OPEN:
                stack.append(symbol)
                continue
            if symbol in CLOSE:
                if stack and stack[-1] == REVERSE_BRACKETS[symbol]:
                    stack.pop()
                else:
                    corrupted.append(symbol)
                    print(f'Expected {BRACKETS[stack[-1]]}, but found {symbol} instead')
                    break
        else:
            stack.reverse()
            completions.append([BRACKETS[x] for x in stack])

    print(f'Errors: {score_errors(corrupted)}')
    print(f'Completion: {score_completion(completions)}')
