"""Seven Segment Search"""


def crack_code(uniques):
    digits = {x: None for x in range(10)}

    digits[1] = [d for d in uniques if len(d) == 2][0]
    digits[7] = [d for d in uniques if len(d) == 3][0]
    digits[4] = [d for d in uniques if len(d) == 4][0]
    digits[8] = [d for d in uniques if len(d) == 7][0]
    digits[9] = [d for d in uniques if len(d) == 6 and set(digits[4]).issubset(d)][0]
    digits[3] = [d for d in uniques if len(d) == 5 and set(digits[1]).issubset(d)][0]

    top = next(iter(set(digits[7]) - set(digits[1])))
    bottom = next(iter(set(digits[9]) - set(digits[4]) - set(top)))
    middle = next(iter(set(digits[3]) - set(digits[1]) - set(top) - set(bottom)))

    digits[0] = [d for d in uniques if len(d) == 6 and not set(middle).issubset(d)][0]
    digits[6] = [d for d in uniques if len(d) == 6 and d not in digits.values()][0]
    digits[5] = [d for d in uniques if len(d) == 5 and set(d).issubset(digits[6])][0]
    digits[2] = [d for d in uniques if len(d) == 5 and d not in digits.values()][0]

    print(digits)
    return digits


def decipher(cipher, output):
    result = ''
    for digit in output:
        for k, v in cipher.items():
            if set(digit) == set(v):
                result += str(k)
                break

    print(result)
    return result


if __name__ == '__main__':
    with open('data2.txt') as f:
        lines = f.readlines()
        entries = [line.rstrip() for line in lines]

    sum = 0
    for entry in entries:

        seg1, seg2 = entry.split(' | ')
        uniques = seg1.split(' ')
        output = seg2.split(' ')

        cipher = crack_code(uniques)
        result = decipher(cipher, output)

        sum += int(result)

    print(f'Sum: {sum}')
