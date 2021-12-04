import numpy as np


def _main():
    puzzle_input = []
    with open('input.txt') as f:
        for line in f.readlines():
            puzzle_input_line = [int(character) for character in line.strip()]
            puzzle_input.append(puzzle_input_line)
    puzzle_input = np.array(puzzle_input)

    # Compute oxygen_generator_rating
    oxygen_generator_rating_string = compute_rating_string(puzzle_input, lambda a, b: a >= b)
    oxygen_generator_rating = int(oxygen_generator_rating_string, 2)

    # Compute co2_scrubber_rating
    inversed_puzzle_input = (~(puzzle_input.astype(bool))).astype(int)
    inversed_co2_scrubber_rating_str = compute_rating_string(inversed_puzzle_input, lambda a, b: a <= b)
    co2_scrubber_rating_string = inversed_co2_scrubber_rating_str.replace('0', '2').replace('1', '0').replace('2', '1')
    co2_scrubber_rating = int(co2_scrubber_rating_string, 2)

    # Display results
    print(oxygen_generator_rating * co2_scrubber_rating)


def compute_rating_string(puzzle_input, comparison_op):
    puzzle_input_copy = puzzle_input.copy()
    for bit_index in range(puzzle_input_copy.shape[1]):
        reference_bit = int(comparison_op(puzzle_input_copy[:, bit_index].sum(), puzzle_input_copy.shape[0] / 2.))
        filter_index = puzzle_input_copy[:, bit_index] == reference_bit
        puzzle_input_copy = puzzle_input_copy[filter_index]
        if puzzle_input_copy.shape[0] == 1:
            break
        elif puzzle_input_copy.shape[0] < 1:
            raise RuntimeError('Oops')
    return str(np.array(puzzle_input_copy, dtype=int))[2:-2].replace(' ', '')


if __name__ == '__main__':
    _main()
