import numpy as np


def _main():
    input_file_name = 'input.txt'
    all_boards, number_sequence = _read_input(input_file_name)
    last_winning_board_idx, marks, last_called_number = _compute_last_winning_board_idx_and_marks(
        all_boards,
        number_sequence
    )

    print("Score:", (all_boards[last_winning_board_idx] * ~marks[last_winning_board_idx]).sum() * last_called_number)


def _compute_last_winning_board_idx_and_marks(all_boards, number_sequence):
    all_boards = all_boards.copy()
    marks = np.zeros(all_boards.shape, dtype=bool)
    all_winning_board_indices = []
    shape = marks.shape
    n_boards = all_boards.shape[0]
    n = None
    for n in number_sequence:
        marks |= all_boards == n

        for board_idx in range(n_boards):
            winner = False
            for column_idx in range(shape[1]):
                winner = marks[board_idx, column_idx, :].all()
                if winner:
                    break

            if not winner:
                for row_idx in range(shape[2]):
                    winner = marks[board_idx, :, row_idx].all()
                    if winner:
                        break
            if winner:
                all_winning_board_indices.append(board_idx)
                if len(all_winning_board_indices) == n_boards:
                    break
                all_boards[board_idx, :, :] = -1
                marks[board_idx, :, :] = False

            if len(all_winning_board_indices) == n_boards:
                break

        if len(all_winning_board_indices) == n_boards:
            break

    if len(all_winning_board_indices) < n_boards:
        loosing_board_indexes = list(set(range(n_boards)) - set(all_winning_board_indices))
        all_loosing_boards = all_boards[loosing_board_indexes]
        raise RuntimeError(f"Following boards never won: {loosing_board_indexes}\n:" + str(all_loosing_boards))

    return all_winning_board_indices[-1], marks, n


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
