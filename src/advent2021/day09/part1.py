def _main():
    # Read input
    with open('input.txt') as f:
        puzzle_input = []
        for line in f.readlines():
            puzzle_input.append([int(number) for number in line.strip()])

    # Find low points' risk levels
    risk_level_sum = 0
    for i in range(len(puzzle_input)):
        for j in range(len(puzzle_input[i])):
            relative_coordinates_to_check = []
            if i > 0:
                relative_coordinates_to_check.append((-1, 0))
            if i < len(puzzle_input) - 1:
                relative_coordinates_to_check.append((1, 0))
            if j > 0:
                relative_coordinates_to_check.append((0, -1))
            if j < len(puzzle_input[i]) - 1:
                relative_coordinates_to_check.append((0, 1))

            # Check is low point
            height = puzzle_input[i][j]
            is_low_point = True
            for c in relative_coordinates_to_check:
                if puzzle_input[i + c[0]][j + c[1]] <= height:
                    is_low_point = False
                    break

            # Update output
            if is_low_point:
                risk_level_sum += height + 1

    print(risk_level_sum)


if __name__ == '__main__':
    _main()
