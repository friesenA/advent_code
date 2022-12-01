"""The Treachery of Whales"""

from statistics import median, mean


def calculate_fuel(positions, target):
    return sum([int(triangle_number(abs(target - position))) for position in positions])


def triangle_number(dimension):
    return ((dimension ** 2) + dimension) / 2


if __name__ == '__main__':
    with open('data.txt') as f:
        line = f.readline().rstrip()
        positions = list(map(int, line.split(',')))

    guess = int(mean(positions))
    fuel_cost = {}
    fuel_cost[guess] = calculate_fuel(positions, guess)
    fuel_cost[guess + 1] = calculate_fuel(positions, guess + 1)
    fuel_cost[guess - 1] = calculate_fuel(positions, guess - 1)

    iterations = 0
    while True:
        iterations += 1
        if fuel_cost[guess] < fuel_cost[guess + 1] and fuel_cost[guess] < fuel_cost[guess -1]:
            break
        elif fuel_cost[guess] < fuel_cost[guess + 1]:
            direction = -1
        else:
            direction = 1

        guess += direction
        fuel_cost[guess + direction] = calculate_fuel(positions, guess + direction)

    print(f'Position: {guess}, with fuel cost: {fuel_cost[guess]}')
    print(iterations)
