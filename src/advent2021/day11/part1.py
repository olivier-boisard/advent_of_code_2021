import numpy as np
import itertools


def _main():
    with open('input.txt') as f:
        puzzle_input = []
        for line in f.readlines():
            line = line.strip()
            puzzle_input.append([int(number) for number in list(line)])
    octopus_grid = np.array(puzzle_input)

    n_steps = 100
    n_flashes = 0
    for _ in range(n_steps):
        n_new_flashes, _ = _flash_octopuses(octopus_grid, np.zeros(octopus_grid.shape, dtype=bool))
        n_flashes += n_new_flashes
        octopus_grid += 1
        octopus_grid[octopus_grid > 9] = 0
    print(n_flashes)


def _flash_octopuses(octopus_grid, flashed_octopuses):
    flashing_octopuses = (octopus_grid >= 9) & ~flashed_octopuses
    n_flashes = flashing_octopuses.sum()
    if flashing_octopuses.any():
        for i, j in zip(*np.where(flashing_octopuses)):
            max_i = octopus_grid.shape[0]
            max_j = octopus_grid.shape[1]
            for ir, jr in itertools.product(range(-1, 2), range(-1, 2)):
                i_to_check = i + ir
                j_to_check = j + jr
                if (not (ir == jr == 0)) and (0 <= i_to_check < max_i) and (0 <= j_to_check < max_j):
                    octopus_grid[i_to_check, j_to_check] += 1
        n_new_flashes, flashing_octopuses = _flash_octopuses(octopus_grid, flashing_octopuses | flashed_octopuses)
        n_flashes += n_new_flashes
    return n_flashes, flashing_octopuses


if __name__ == '__main__':
    _main()
