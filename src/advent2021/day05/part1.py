import numpy as np


def _main():
    segments = []
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            points = line.split(' -> ')
            start_coordinates = [int(n) for n in points[0].split(',')]
            stop_coordinates = [int(n) for n in points[1].split(',')]

            # Consider only horizontal and vertical lines
            if start_coordinates[0] == stop_coordinates[0] or start_coordinates[1] == stop_coordinates[1]:
                segments.append([start_coordinates, stop_coordinates])

    # Initialize diagram
    segments = np.array(segments)
    if (segments < 0).any():
        raise RuntimeError("Oops")
    max_coordinate = np.max(segments)
    marks = np.zeros((max_coordinate + 1, max_coordinate + 1))

    # Add marks to diagram
    for segment in segments:
        if np.any(segment[0, :] > segment[1, :]):
            segment = segment[::-1, :]
        marks[segment[0, 0]:segment[1, 0] + 1, segment[0, 1]:segment[1, 1] + 1] += 1

    # Display results
    print((marks >= 2).sum())


if __name__ == '__main__':
    _main()
