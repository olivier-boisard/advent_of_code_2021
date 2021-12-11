import numpy as np
import itertools


def _main():
    with open('input.txt') as f:
        puzzle_input = []
        for line in f.readlines():
            line = line.strip()
            puzzle_input.append([int(number) for number in list(line)])
    octopus_grid = np.array(puzzle_input)

    step = 0
    while True:
        _flash_octopuses(octopus_grid, np.zeros(octopus_grid.shape, dtype=bool))
        octopus_grid += 1
        octopus_grid[octopus_grid > 9] = 0
        step += 1
        if (octopus_grid == 0).all():
            break
    print(step)


def _flash_octopuses(octopus_grid, flashed_octopuses):
    flashing_octopuses = (octopus_grid >= 9) & ~flashed_octopuses
    if flashing_octopuses.any():
        for i, j in zip(*np.where(flashing_octopuses)):
            max_i = octopus_grid.shape[0]
            max_j = octopus_grid.shape[1]
            for ir, jr in itertools.product(range(-1, 2), range(-1, 2)):
                i_to_check = i + ir
                j_to_check = j + jr
                if (not (ir == jr == 0)) and (0 <= i_to_check < max_i) and (0 <= j_to_check < max_j):
                    octopus_grid[i_to_check, j_to_check] += 1
        _flash_octopuses(octopus_grid, flashing_octopuses | flashed_octopuses)


if __name__ == '__main__':
    _main()
