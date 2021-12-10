import numpy as np


def _main():
    with open('input.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    autocompletes = _extract_autocompletes(lines)
    score = _compute_score(autocompletes)
    print(score)


def _extract_autocompletes(lines):
    autocompletes = []
    for line in lines:
        remaining_opening_characters = _extract_remaining_characters(line)
        autocomplete_characters = _extract_autocomplete_characters(remaining_opening_characters)
        autocompletes.append(autocomplete_characters)
    return autocompletes


def _extract_remaining_characters(line):
    remaining_opening_characters = []
    opening_characters = '([<{'
    for character in line:
        if character in opening_characters:
            remaining_opening_characters.append(character)
        elif _valid_closing_parameter(remaining_opening_characters, character):
            remaining_opening_characters.pop()
        else:
            remaining_opening_characters = None
            break
    return remaining_opening_characters


def _valid_closing_parameter(found_opening_characters, character):
    closing_to_opening_characters = {')': '(', ']': '[', '>': '<', '}': '{'}
    if len(found_opening_characters) == 0:
        return False
    return closing_to_opening_characters[character] == found_opening_characters[-1]


def _extract_autocomplete_characters(remaining_opening_characters):
    autocomplete_characters = []
    if remaining_opening_characters is not None:
        opening_to_closing_characters = {'(': ')', '<': '>', '{': '}', '[': ']'}
        autocomplete_characters = [opening_to_closing_characters[c] for c in remaining_opening_characters[::-1]]
    return autocomplete_characters


def _compute_score(autocompletes):
    score_per_autocomplete = []
    for autocomplete in autocompletes:
        if len(autocomplete) > 0:
            score = 0
            for character in autocomplete:
                score *= 5
                score += {')': 1, ']': 2, '}': 3, '>': 4}[character]
            score_per_autocomplete.append(score)
    score = int(np.median(score_per_autocomplete))
    return score


if __name__ == '__main__':
    _main()
