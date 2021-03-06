import pandas as pd


def _main():
    with open('input.txt') as f:
        puzzle_input = [int(line) for line in f.readlines()]
    n_increases = (pd.Series(puzzle_input).rolling(3).sum().dropna().diff() > 0).sum()
    print(f'Number of increases: {n_increases}')


if __name__ == '__main__':
    _main()
