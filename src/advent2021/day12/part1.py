from dataclasses import dataclass, field
from typing import Set, Dict


def _main():
    connections = _load_puzzle_input()
    graph = _build_graph(connections)
    print(_walk_graph(graph, 'start'))


@dataclass
class Cave:
    is_big: bool
    connected_caves: Set[str] = field(default_factory=set)
    visited: bool = False

    @property
    def can_be_visited(self):
        return self.is_big or not self.visited


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
        graph[cave_in] = Cave(is_big=cave_in.isupper())
    graph[cave_in].connected_caves.add(cave_out)


def _walk_graph(graph, start_cave):
    if start_cave == 'end':
        return 1
    n_paths = 0
    current_cave = graph[start_cave]
    current_cave.visited = True
    for next_cave in sorted(current_cave.connected_caves):
        if graph[next_cave].can_be_visited:
            n_paths += _walk_graph(graph, next_cave)
    current_cave.visited = False
    return n_paths


if __name__ == '__main__':
    _main()
