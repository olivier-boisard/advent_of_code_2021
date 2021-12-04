import numpy as np


def _main():
    input_file_name = 'input.txt'
    all_boards, number_sequence = _read_input(input_file_name)
    board_idx, marks, last_called_number = _compute_winning_board_idx_and_marks(all_boards, number_sequence)

    print("Score:", (all_boards[board_idx] * ~marks[board_idx]).sum() * last_called_number)


def _compute_winning_board_idx_and_marks(all_boards, number_sequence):
    marks = np.zeros(all_boards.shape, dtype=bool)
    winner = False
    board_idx = None
    n = None
    for n in number_sequence:
        marks |= all_boards == n

        shape = marks.shape
        for board_idx in range(shape[0]):
            for column_idx in range(shape[1]):
                winner = marks[board_idx, column_idx, :].all()
                if winner:
                    break
            if winner:
                break
            for row_idx in range(shape[2]):
                winner = marks[board_idx, :, row_idx].all()
                if winner:
                    break
            if winner:
                break
        if winner:
            break
    if not winner:
        raise Exception('Oops')
    return board_idx, marks, n


def _read_input(input_file_name):
    with open(input_file_name) as f:
        lines = f.readlines()
        number_sequence = [int(n.strip()) for n in lines[0].split(',')]

        all_boards = []
        current_board = []
        for line in lines[2:]:
            # Create board
            line_as_number_strings = line.strip().split(' ')
            if len(line_as_number_strings[0]) > 0:
                line_as_numbers = [int(n.strip()) for n in line_as_number_strings if n != '']
                current_board.append(line_as_numbers)
            else:
                all_boards.append(current_board)
                current_board = []
    all_boards.append(current_board)
    return np.array(all_boards), number_sequence


if __name__ == '__main__':
    _main()
