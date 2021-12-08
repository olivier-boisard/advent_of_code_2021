import numpy as np


def _main():
    with open('input.txt') as f:
        puzzle_input = [line.strip() for line in f.readlines()]

    output_numbers = []
    for entry in puzzle_input:
        signals, outputs = _retrieve_ios(entry)
        digits_to_pattern = _retrieve_trivial_digits_to_patterns(signals)
        rewire_mapping = _build_rewire_mapping(digits_to_pattern, signals)
        output_numbers.append(_decode_screen_output(outputs, rewire_mapping))
    print(np.sum(output_numbers))


def _retrieve_ios(entry):
    entry_elements = entry.split(' | ')
    signals = entry_elements[0].split(' ')
    outputs = entry_elements[1].split(' ')
    return signals, outputs


def _retrieve_trivial_digits_to_patterns(signals):
    segment_lengths_to_trivial_digits = {2: 1, 3: 7, 4: 4, 7: 8}
    digits_to_pattern = {}
    for pattern in signals:
        pattern_length = len(pattern)
        if pattern_length in segment_lengths_to_trivial_digits:
            digits_to_pattern[segment_lengths_to_trivial_digits[pattern_length]] = pattern
    return digits_to_pattern


def _build_rewire_mapping(digits_to_pattern, signals):
    rewire_mapping = {}
    for character in 'abcdefg':
        n_appearances = _count_character_appearances(character, signals)
        n_appearances_to_letter = {4: 'e', 6: 'b', 9: 'f'}
        if n_appearances in n_appearances_to_letter:
            rewire_mapping[character] = n_appearances_to_letter[n_appearances]
        elif n_appearances == 8:
            rewire_mapping[character] = 'c' if character in digits_to_pattern[1] else 'a'
        elif n_appearances == 7:
            rewire_mapping[character] = 'd' if character in digits_to_pattern[4] else 'g'
    return rewire_mapping


def _count_character_appearances(character, patterns):
    output = 0
    for pattern in patterns:
        if character in pattern:
            output += 1
    return output


def _decode_screen_output(outputs, rewire_mapping):
    output_digits = []
    for output in outputs:
        output_digits.append(_decode_pattern(rewire_mapping, output))
    output_number = int(''.join(output_digits))
    return output_number


def _decode_pattern(rewire_mapping, pattern):
    rewired_output = ''.join(sorted([rewire_mapping[character] for character in pattern]))
    pattern_to_digit = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9'
    }
    return pattern_to_digit[rewired_output]


if __name__ == '__main__':
    _main()
