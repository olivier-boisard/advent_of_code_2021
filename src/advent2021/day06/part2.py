import numpy as np


def _main():
    with open('input.txt') as f:
        fishes = np.array([int(n) for n in f.readlines()[0].split(',')])

    # Naive solution
    simulation_duration_in_days = 256
    n_fishes = _run_simulation(fishes, simulation_duration_in_days)
    print(n_fishes)


def _run_simulation(fishes, simulation_duration_in_days):
    buffer = _initialize_buffer(fishes)
    for i in range(simulation_duration_in_days):
        n_new_fishes = buffer[0]
        buffer = np.concatenate([buffer[1:], np.array([n_new_fishes])])
        buffer[6] += n_new_fishes
    return buffer.sum()


def _initialize_buffer(fishes):
    buffer = np.zeros(9, dtype=np.int64)
    for fish in fishes:
        buffer[fish] += 1
    return buffer


if __name__ == '__main__':
    _main()
