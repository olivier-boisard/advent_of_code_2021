import itertools


def _main():
    with open('input.txt') as f:
        puzzle_input = [line.split(' | ')[1].strip().split(' ') for line in f.readlines()]
    puzzle_input = list(itertools.chain(*puzzle_input))
    n_segments_in_digits_of_interest = [2, 3, 4, 7]

    output = 0
    for segments in puzzle_input:
        if len(segments) in n_segments_in_digits_of_interest:
            output += 1
    print(output)


if __name__ == '__main__':
    _main()
