import itertools
import numpy as np
import pandas as pd


def _main():
    puzzle_input = _read_input()
    basins = _initialize_basins(puzzle_input)
    basins = _map_basins(basins, puzzle_input)
    _display_results(basins)


def _read_input():
    with open('input.txt') as f:
        puzzle_input = []
        for line in f.readlines():
            puzzle_input.append([int(number) for number in line.strip()])
    return puzzle_input


def _initialize_basins(puzzle_input):
    basins = np.zeros((len(puzzle_input), len(puzzle_input[0])), dtype=int)
    current_basin_id = 1
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            if basins[i, j] > 0:
                continue

            relative_coordinates_to_check = _build_relative_coordinates_to_check(
                i,
                j,
                len(puzzle_input) - 1,
                len(puzzle_input[i]) - 1
            )

            # Check is low point
            height = puzzle_input[i][j]
            is_low_point = True
            for c in relative_coordinates_to_check:
                if puzzle_input[i + c[0]][j + c[1]] <= height:
                    is_low_point = False
                    break

            # Update basin id
            if is_low_point:
                basins[i][j] = current_basin_id
                current_basin_id += 1
    return basins


def _map_basins(basins, puzzle_input):
    basins = basins.copy()
    while (basins == 0).any():
        for i, j in itertools.product(range(basins.shape[0]), range(basins.shape[1])):
            if basins[i, j] == 0:
                _assign_basin_id_inplace(basins, puzzle_input, i, j)
    return basins


def _assign_basin_id_inplace(basins, puzzle_input, i, j):
    if puzzle_input[i][j] == 9:
        basins[i, j] = -1
    else:
        relative_coordinates_to_check = _build_relative_coordinates_to_check(
            i,
            j,
            basins.shape[0] - 1,
            basins.shape[1] - 1
        )
        for c in relative_coordinates_to_check:
            i_c = i + c[0]
            j_c = j + c[1]
            if puzzle_input[i_c][j_c] < puzzle_input[i][j]:
                basins[i, j] = basins[i_c, j_c]
                break


def _build_relative_coordinates_to_check(i, j, max_i, max_j):
    relative_coordinates_to_check = []
    if i > 0:
        relative_coordinates_to_check.append((-1, 0))
    if i < max_i:
        relative_coordinates_to_check.append((1, 0))
    if j > 0:
        relative_coordinates_to_check.append((0, -1))
    if j < max_j:
        relative_coordinates_to_check.append((0, 1))
    return relative_coordinates_to_check


def _display_results(basins):
    basins = basins.ravel()
    basins = basins[basins != -1]
    print(pd.Series(basins.ravel()).value_counts().sort_values().tail(3).prod())


if __name__ == '__main__':
    _main()
