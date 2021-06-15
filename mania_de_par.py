from collections import defaultdict


class Graph:
    """
    Problem: https://www.urionlinejudge.com.br/repository/UOJ_1931.html

    Solution: Finds all valid paths given a destination node
    and computes the minimum cost.

    DFS algorithm derived from: https://www.geeksforgeeks.org/find-paths-given-source-destination/

    Test Cases:

    >>> edges = [
        (1, 2, 2),
        (2, 3, 1),
        (2, 4, 10),
        (3, 4, 6)
    ]
    >>> g = Graph(4, edges)
    >>> g.run()
    output: 12

    >>> edges = [
        (1, 2, 3),
        (2, 3, 5),
        (3, 5, 2),
        (5, 1, 8),
        (2, 4, 1),
        (4, 5, 4)
    ]
    >>> g = Graph(5, edges)
    >>> g.run()
    output: -1

    """
    def __init__(self, vertices: list, edges: list) -> None:
        self.vertices = vertices
        self.edges = edges
        self.graph = defaultdict(list)
        self.weights = {}
        self.visited = [False] * vertices
        self.paths = []

        self._build_graph()

    def add_edge(self, u: int, v: int, w: int) -> None:
        # builds the adjacency list
        self.graph[u].append(v)
        self.weights[(u,v)] = w

    def _build_graph(self) -> None:
        for u,v,w in self.edges:
            self.add_edge(u, v, w)
            # for undirected graphs
            self.add_edge(v, u, w)

    def find_paths(self, u: int, d: int, path: list) -> None:
        self.visited[u-1] = True
        path.append(u)

        if u == d and self._is_valid_path(path):
            valid_path = path.copy()
            self.paths.append(valid_path)
        else:
            for i in self.graph[u]:
                if self.visited[i-1] == False:
                    self.find_paths(i, d, path)

        path.pop()
        self.visited[u-1] = False

    def get_path_cost(self, path: list)  -> int:
        """ Computes the cost of a path.

        Given a path with nodes list
        and the dictionary containing the edges pairs as keys
        and the weight cost as value
        """
        weights = []
        for idx in range(len(path)):
            value = path[idx]
            try:
                next = path[idx+1]
                weight = self.weights.get((value, next))
                weights.append(weight)
            except IndexError:
                pass

        return sum(weights)

    def run(self) -> int:
        path = []

        start = 1
        dest = self.vertices

        self.find_paths(start, dest, path)

        if not self.paths:
            # if there's no valid path, returns -1
            return -1

        path_costs = []
        for valid_path in self.paths:
            cost = self.get_path_cost(valid_path)
            path_costs.append(cost)

        return min(path_costs)

    def _is_valid_path(self, path: list) -> bool:
        """ Validates if a given path is valid.

        According to the problem, a valid path must have
        an even number of edges
        """
        number_of_edges = len(path) - 1

        return number_of_edges % 2 == 0
