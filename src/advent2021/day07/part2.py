import numpy as np


def _main():
    with open('input.txt') as f:
        horizontal_positions = np.array([int(n) for n in f.readlines()[0].split(',')], dtype=int)

    best_position = None
    min_cost_in_fuel = None
    for position in range(np.min(horizontal_positions), np.max(horizontal_positions) + 1):
        distances = np.abs(horizontal_positions - position)
        cost_in_fuel = int((distances * (1 + distances) / 2).sum())
        if min_cost_in_fuel is None:
            min_cost_in_fuel = cost_in_fuel
        elif cost_in_fuel < min_cost_in_fuel:
            best_position = position
            min_cost_in_fuel = cost_in_fuel

    print(best_position)
    print(min_cost_in_fuel)


if __name__ == '__main__':
    _main()
