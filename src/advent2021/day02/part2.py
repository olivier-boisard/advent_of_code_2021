def _main():
    with open('input.txt') as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    horizontal_coordinate = 0
    depth_coordinate = 0
    aim = 0
    for line in puzzle_input:
        elements = line.split(' ')
        direction = elements[0]
        speed = int(elements[1])
        if direction == 'forward':
            horizontal_coordinate += speed
            depth_coordinate += aim * speed
        elif direction == 'up':
            aim -= speed
        elif direction == 'down':
            aim += speed
        else:
            raise RuntimeError(f'Unknown direction "{depth_coordinate}"')

    print(horizontal_coordinate * depth_coordinate)


if __name__ == '__main__':
    _main()
