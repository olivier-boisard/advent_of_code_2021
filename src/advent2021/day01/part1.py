import numpy as np
import os


def _main():
    with open(os.path.join('day01', 'input.txt')) as f:
        puzzle_input = [int(line) for line in f.readlines()]
    n_increases = (np.diff(puzzle_input) > 0).sum()
    print(f'Number of increases: {n_increases}')


if __name__ == '__main__':
    _main()
