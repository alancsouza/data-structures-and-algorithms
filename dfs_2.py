"""
problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=272
"""

from collections import defaultdict


class Graph:
    """ Computes the number of edges that are not reachable

    Given a Graph, a TTL (time to live) and a starting point node

    Usage:

    >>> g = Graph(starting_point=3, ttl=2, edges=edges)

    >>> g.run()
    Output:

    3 nodes not reachable from node 3 with TTL = 2
    """
    def __init__(
        self,
        starting_point: int,
        ttl: int,
        edges: list = []
    ) -> None:
        self.graph = defaultdict(list)

        self.starting_point = starting_point
        # Time To Live
        self.ttl = ttl
        self.edges = edges
        self.reachable_nodes = []

    def add_edge(self, u: int, v: int) -> None:
        self.graph[u].append(v)

    def get_reachable_nodes(self, v: int, ttl: int) -> None:
        """Recursive method to find the reachable nodes

        Given a Time to Live (ttl)
        """
        if ttl == 0:
            return
        elif ttl == 1:
            self.reachable_nodes.extend(self.graph[v])
        else:
            for neighbour in self.graph[v]:
                self.reachable_nodes.append(neighbour)
                self.get_reachable_nodes(v=neighbour, ttl=ttl-1)

    def run(self) -> None:
        if not all([self.starting_point, self.ttl]):
            return

        self._build_graph()

        number_of_nodes = len(self.graph)

        self.get_reachable_nodes(v=self.starting_point, ttl=self.ttl)

        number_of_reachable_nodes = len(list(set(self.reachable_nodes)))

        not_reachable_nodes = number_of_nodes - number_of_reachable_nodes

        print(f"{not_reachable_nodes} nodes not reachable from node {self.starting_point} with TTL = {self.ttl}")

    def _build_graph(self) -> None:
        for u,v in self.edges:
            self.add_edge(u,v)

            # for undirected graphs
            # check if there are cycles:
            if not (v,u) in self.edges:
                self.add_edge(v,u)

"""
Test case 1:

>>> edges = [
    (10, 15),
    (15, 20),
    (20, 25),
    (10, 30),
    (30, 47),
    (47, 50),
    (25, 45),
    (45, 65),
    (15, 35),
    (35, 55),
    (20, 40),
    (50, 55),
    (35, 40),
    (55, 60),
    (40, 60),
    (60, 65)
]

Test case 2:

>>> edges = [
    (1, 2),
    (2, 7),
    (1, 3),
    (3, 4),
    (3, 5),
    (5, 10),
    (5, 11),
    (4, 6),
    (7, 6),
    (7, 8),
    (7, 9),
    (8, 9),
    (8, 6),
    (6, 11)
]
"""
