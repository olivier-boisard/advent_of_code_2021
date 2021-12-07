import numpy as np


def _main():
    with open('input.txt') as f:
        horizontal_positions = np.array([int(n) for n in f.readlines()[0].split(',')], dtype=int)

    best_position = np.median(horizontal_positions)
    cost_in_fuel = int(np.abs(horizontal_positions - best_position).sum())
    print(cost_in_fuel)


if __name__ == '__main__':
    _main()
