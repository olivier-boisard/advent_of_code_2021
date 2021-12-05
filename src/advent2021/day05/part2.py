import numpy as np
import copy


def _main():
    non_diagonal_segments = []
    diagonal_segments = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            points = line.split(' -> ')
            start_coordinates = [int(n) for n in points[0].split(',')]
            stop_coordinates = [int(n) for n in points[1].split(',')]

            if start_coordinates[0] == stop_coordinates[0] or start_coordinates[1] == stop_coordinates[1]:
                non_diagonal_segments.append([start_coordinates, stop_coordinates])
            else:
                diagonal_segments.append([start_coordinates, stop_coordinates])
    non_diagonal_segments = np.array(non_diagonal_segments)
    diagonal_segments = np.array(diagonal_segments)

    # Initialize diagram
    if (non_diagonal_segments < 0).any() or (diagonal_segments < 0).any():
        raise RuntimeError("Oops")
    max_coordinate = np.max(non_diagonal_segments)
    marks = np.zeros((max_coordinate + 1, max_coordinate + 1))

    # Add marks to diagram
    for segment in non_diagonal_segments:
        if np.any(segment[0, :] > segment[1, :]):
            segment = segment[::-1, :]
        marks[segment[0, 0]:segment[1, 0] + 1, segment[0, 1]:segment[1, 1] + 1] += 1

    for segment in diagonal_segments:
        incrementer = ((segment[1, :] - segment[0, :]) > 0) * 2 - 1
        current_mark = copy.deepcopy(segment[0, :])
        while np.any(current_mark != segment[1, :]):
            marks[current_mark[0], current_mark[1]] += 1
            current_mark += incrementer
        marks[current_mark[0], current_mark[1]] += 1

    # Display results
    print((marks >= 2).sum())


if __name__ == '__main__':
    _main()
