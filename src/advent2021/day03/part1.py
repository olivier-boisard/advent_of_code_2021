import numpy as np


def _main():
    puzzle_input = []
    with open('input.txt') as f:
        for line in f.readlines():
            puzzle_input_line = [int(character) for character in line.strip()]
            puzzle_input.append(puzzle_input_line)
    puzzle_input = np.array(puzzle_input)

    # Compute gamma rate
    gamma_rate_string = []
    for vertical_slice in puzzle_input.transpose():
        gamma_rate_string.append(vertical_slice.sum() > vertical_slice.shape[0] // 2)
    gamma_rate_string = str(np.array(gamma_rate_string, dtype=int))[1:-1].replace(' ', '')
    gamma_rate = int(gamma_rate_string, 2)

    # Compute epsilon rate
    epsilon_rate_string = gamma_rate_string.replace('0', '2').replace('1', '0').replace('2', '1')
    epsilon_rate = int(epsilon_rate_string, 2)

    print(gamma_rate * epsilon_rate)


if __name__ == '__main__':
    _main()
