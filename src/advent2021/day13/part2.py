import numpy as np
from dataclasses import dataclass


@dataclass
class Fold:
    axis: str
    coordinate: int


def _main():
    dot_coordinates, folds = _read_input()
    grid = _build_grid(dot_coordinates)
    grid = _fold_grid(grid, folds)
    print(grid.transpose()[::-1])


def _read_input():
    with open('input.txt') as f:
        dot_coordinates = []
        folds = []
        read_dots_state = 'read dots'
        read_fold_state = 'read fold'
        state = read_dots_state
        for line in f.readlines():
            if state == read_dots_state:
                line = line.strip()
                if line == '':
                    state = read_fold_state
                else:
                    dot_coordinates.append([int(coordinate) for coordinate in line.split(',')])
            elif state == read_fold_state:
                fold_elements = line.strip().split(' ')[-1].split('=')
                folds.append(Fold(axis=fold_elements[0], coordinate=int(fold_elements[1])))
            else:
                raise RuntimeError('Oops')
    return dot_coordinates, folds


def _build_grid(dot_coordinates):
    dot_coordinates = np.array(dot_coordinates)
    max_x = dot_coordinates[:, 0].max()
    max_y = dot_coordinates[:, 1].max()
    grid = np.zeros((max_x + 1, max_y + 1), dtype=bool)
    grid[dot_coordinates[:, 0], dot_coordinates[:, 1]] = True
    return grid


def _fold_grid(grid, folds):
    for fold in folds:
        if fold.axis == 'x':
            left_part = grid[:fold.coordinate, :]
            right_part = grid[fold.coordinate + 1:, :]
            if left_part.shape[0] < right_part.shape[0]:
                left_part = np.concatenate([
                    np.zeros((right_part.shape[0] - left_part.shape[0], left_part.shape[1]), dtype=bool),
                    left_part
                ])
            elif right_part.shape[0] < left_part.shape[0]:
                right_part = np.concatenate([
                    right_part,
                    np.zeros((left_part.shape[0] - right_part.shape[0], right_part.shape[1]), dtype=bool)
                ])
            grid = left_part | right_part[::-1, :]
        elif fold.axis == 'y':
            up_part = grid[:, :fold.coordinate]
            down_part = grid[:, fold.coordinate + 1:]

            if up_part.shape[1] < down_part.shape[1]:
                up_part = np.concatenate([
                    np.zeros((up_part.shape[0], (down_part.shape[1] - up_part.shape[1])), dtype=bool),
                    up_part
                ], axis=1)
            elif down_part.shape[1] < up_part.shape[1]:
                down_part = np.concatenate([
                    down_part,
                    np.zeros((down_part.shape[0], (up_part.shape[1] - down_part.shape[1])), dtype=bool)
                ], axis=1)
            grid = up_part | down_part[:, ::-1]
        else:
            raise RuntimeError('Oops')
    return grid


if __name__ == '__main__':
    _main()
