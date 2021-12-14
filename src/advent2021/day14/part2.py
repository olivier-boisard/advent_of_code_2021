import pandas as pd
import numpy as np


def _main():
    n_steps = 40

    chain, rules = _read_input()
    count = _count_polymer_components(chain, rules, n_steps)
    print(count.max() - count.min())


def _read_input():
    with open('input.txt') as f:
        lines = f.readlines()
    chain = lines[0].strip()
    rules = {}
    for line in lines[2:]:
        rule_elements = line.strip().split(' -> ')
        rules[rule_elements[0]] = rule_elements[1]
    return chain, rules


def _count_polymer_components(pattern, rules, remaining_steps, levels_to_patterns_to_counts=None):
    if remaining_steps == 0:
        series = pd.Series(list(pattern)).value_counts()
        series.name = 'count'
        return series

    if levels_to_patterns_to_counts is None:
        levels_to_patterns_to_counts = {}
    if remaining_steps not in levels_to_patterns_to_counts:
        levels_to_patterns_to_counts[remaining_steps] = {}

    total_count = pd.Series(name='count', dtype=np.int64)
    for i in range(len(pattern) - 1):
        sub_chain = pattern[i:i + 2]
        if sub_chain in levels_to_patterns_to_counts[remaining_steps]:
            sub_count = levels_to_patterns_to_counts[remaining_steps][sub_chain]
        else:
            new_chain = ''.join([sub_chain[0], rules[sub_chain], sub_chain[1]])
            sub_count = _count_polymer_components(new_chain, rules, remaining_steps - 1, levels_to_patterns_to_counts)
            sub_count[sub_chain[0]] -= 1
            levels_to_patterns_to_counts[remaining_steps][sub_chain] = sub_count
        total_count = pd.merge(
            total_count,
            sub_count,
            left_index=True,
            right_index=True,
            how='outer'
        ).fillna(0).astype(np.int64).sum(axis=1)
        total_count.name = 'count'
    total_count[pattern[0]] += 1
    return total_count


if __name__ == '__main__':
    _main()
