from dataclasses import dataclass, field
from typing import Set


def _main():
    connections = _load_puzzle_input()
    graph = _build_graph(connections)
    print(_walk_graph(graph, 'start'))


@dataclass
class Cave:
    is_big: bool
    start_or_end: bool = False
    connected_caves: Set[str] = field(default_factory=set)
    n_visits: int = 0

    def can_be_visited(self, is_single_small_cave_visited_twice):
        if self.start_or_end and self.n_visits > 0:
            return False
        n_visits_is_valid = (self.n_visits == 0) or (not is_single_small_cave_visited_twice and self.n_visits < 2)
        return self.is_big or n_visits_is_valid


def _load_puzzle_input():
    with open('input.txt') as f:
        connections = [line.strip() for line in f.readlines()]
    return connections


def _build_graph(connections):
    graph = {}
    for connection in connections:
        cave_1, cave_2 = connection.split('-')
        _add_caves_to_graph(cave_1, cave_2, graph)
        _add_caves_to_graph(cave_2, cave_1, graph)
    return graph


def _add_caves_to_graph(cave_in, cave_out, graph):
    if cave_in not in graph:
        graph[cave_in] = Cave(is_big=cave_in.isupper(), start_or_end=cave_in in ['start', 'end'])
    graph[cave_in].connected_caves.add(cave_out)


def _walk_graph(graph, start_cave, is_single_small_cave_visited_twice=False):
    if start_cave == 'end':
        return 1
    n_paths = 0
    current_cave = graph[start_cave]
    current_cave.n_visits += 1
    is_single_small_cave_visited_twice |= not current_cave.is_big and current_cave.n_visits == 2
    for next_cave in sorted(current_cave.connected_caves):
        if graph[next_cave].can_be_visited(is_single_small_cave_visited_twice):
            n_paths += _walk_graph(
                graph,
                next_cave,
                is_single_small_cave_visited_twice=is_single_small_cave_visited_twice
            )
    current_cave.n_visits -= 1
    return n_paths


if __name__ == '__main__':
    _main()
