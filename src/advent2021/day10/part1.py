import numpy as np


def _main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    first_illegal_character_per_line = _extract_first_illegal_character_per_line(lines)
    score = _compute_scores(first_illegal_character_per_line)
    print(score)


def _extract_first_illegal_character_per_line(lines):
    opening_characters = '([<{'
    first_illegal_character_per_line = []
    for line in lines:
        found_opening_characters = []
        for character in line:
            if character in opening_characters:
                found_opening_characters.append(character)
            elif _valid_closing_parameter(found_opening_characters, character):
                found_opening_characters.pop()
            else:
                first_illegal_character_per_line.append(character)
                break
    return first_illegal_character_per_line


def _compute_scores(first_illegal_character_per_line):
    score_mapping = {')': 3, ']': 57, '}': 1197, '>': 25137}
    return np.sum([score_mapping[character] for character in first_illegal_character_per_line])


def _valid_closing_parameter(found_opening_characters, character):
    closing_to_opening_characters = {')': '(', ']': '[', '>': '<', '}': '{'}
    if len(found_opening_characters) == 0:
        return False
    return closing_to_opening_characters[character] == found_opening_characters[-1]


if __name__ == '__main__':
    _main()
