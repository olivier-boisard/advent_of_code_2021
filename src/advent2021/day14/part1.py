import pandas as pd


def _main():
    n_steps = 10

    chain, rules = _read_input()
    chain = _build_polymer(chain, rules, n_steps)
    print(_process_output(chain))


def _read_input():
    with open('input.txt') as f:
        lines = f.readlines()
    chain = lines[0].strip()
    rules = {}
    for line in lines[2:]:
        rule_elements = line.strip().split(' -> ')
        rules[rule_elements[0]] = rule_elements[1]
    return chain, rules


def _build_polymer(pattern, rules, n_steps):
    for _ in range(n_steps):
        new_chain = [pattern[0]]
        for i in range(len(pattern) - 1):
            sub_chain = pattern[i:i + 2]
            new_chain += [rules[sub_chain], sub_chain[1]]
        pattern = ''.join(new_chain)
    return pattern


def _process_output(chain):
    counts = pd.Series(list(chain)).value_counts()
    return counts.max() - counts.min()


if __name__ == '__main__':
    _main()
