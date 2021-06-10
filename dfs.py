""" Depth-first search algorithm:

problem: https://www.urionlinejudge.com.br/repository/UOJ_1076.html

Implementation derived from https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

"""

from collections import defaultdict


class Graph:
    """Constructs a adjaceny list and enables the DFS traversal

    usage:

    Given a list of edges:

    >>> edges = [(1, 2), (1, 4), (4, 7), (7, 8), (4, 1), (4, 3)]

    Given the starting node: In this case, 2:
    >>> g = Graph(starting_point=1, edges=edges)

    >>> g.run()

    Output:

    Prints the visited nodes and the total operations (moves)

    e.g:

    node visited: 1
    node visited: 2
    node visited: 4
    node visited: 7
    node visited: 8
    node visited: 3
    The number of operations is 10
    """
    def __init__(self, starting_point: int, edges: list = []) -> None:
        self.graph = defaultdict(list)
        self.number_of_operations = 0
        self.starting_point = starting_point
        # edges must be a list of tuples containing the two connected vertices
        self.edges = edges

    def add_edge(self, u:int, v:int) -> None:
        # creates the adjacency list from u and v node labels
        self.graph[u].append(v)

    def dfs_util(self, v: int, visited: set) -> None:
        # mark the current node as visited
        visited.add(v)

        print(f"node visited: {v}")

        # recur for all the adjacent vertices
        for neighbour in self.graph[v]:
            # updates the number of operations (moves)
            self.number_of_operations += 1

            if neighbour not in visited:
                self.dfs_util(neighbour, visited)


    def dfs(self, v:int) -> None:
        # create a set to store visited vertices
        visited = set()

        self.dfs_util(v, visited)

        print(f"The number of operations is {self.number_of_operations}")

    def run(self) -> None:
        for u,v in self.edges:
            self.add_edge(u,v)

            # for undirected graphs
            # check if there are cycles:
            if not (v,u) in self.edges:
                self.add_edge(v,u)

        self.dfs(v=self.starting_point)


"""
Test cases
>>> Test Case 1:
>>> edges = [
    (0 ,4),
    (2 ,3),
    (6 ,2),
    (8 ,9),
    (10, 9),
    (8 ,12),
    (14, 15),
    (14, 10),
    (6 ,5),
    (10, 11),
    (11, 7),
    (4 ,8),
    (0 ,1),
    (1 ,2),
    (12, 13)
]

>>> Test Case 2:
edges = [
    (1, 2),
    (1, 4),
    (4, 7),
    (7, 8),
    (4, 1),
    (4, 3)
]

"""