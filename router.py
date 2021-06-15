import sys


class Graph:
    """
    Problem: https://www.urionlinejudge.com.br/repository/UOJ_1774.html

    Prim's algorithm implementation derived from:
    https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/

    Finds the minimum spanning tree using the Prim algorithm.

    Given the number of nodes (size), and the edges, which is
    a List containing tuples with the vertex pair (u,v) and the edge weight.

    Test Case:

    >>> edges = [
        (1, 3, 6),
        (1, 4, 9),
        (2, 3, 17),
        (2, 5, 32),
        (2, 7, 27),
        (3, 4, 11),
        (3, 5, 4),
        (4, 5, 3),
        (4, 6, 19),
        (5, 6, 13),
        (5, 7, 15),
        (6, 7, 5)
    ]

    >>> g = Graph(7, edges)
    >>> g.prim_mst()
    output:
    Edge 	 Weight
    2->1 	 17
    0->2 	 6
    4->3 	 3
    2->4 	 4
    4->5 	 13
    5->6 	 5
    The total cost of the network is 48

    """
    def __init__(self, size: int, edges: list) -> None:
        self.vertices = size
        self.edges = edges
        self.dist = [sys.maxsize] * size
        # minimum spanning tree
        self.mst = [False] * size
        # array to store constructed MST
        self.parent = [None] * size
        self.weights = []
        self._build_graph()


    def min_dist(self) -> int:
        min = sys.maxsize # infinite-like value
        min_idx = None

        for v in range(self.vertices):
            if self.dist[v] < min and self.mst[v] == False:
                min = self.dist[v]
                min_idx = v

        return min_idx

    def prim_mst(self) -> None:
        self.dist[0] = 0

        # first node is always the root
        self.parent[0] = -1

        for _ in range(self.vertices):
            u = self.min_dist()

            if u is not None:
                self.mst[u] = True

                for v in range(self.vertices):
                    if self._should_update_dist_value(u,v):
                        self.dist[v] = self.graph[u][v]
                        self.parent[v] = u

        self._print_solution()

    def _should_update_dist_value(self, u: int, v: int) -> bool:
        return (
            self.graph[u][v] > 0
            and self.mst[v] == False
            and self.dist[v] > self.graph[u][v]
        )

    def _print_solution(self) -> None:
        print("Edge \t Weight")
        for node in range(1, self.vertices):
            parent = self.parent[node]
            weight = self.graph[node][parent]
            print(f"{parent}->{node} \t {weight}")
            self.weights.append(weight)

        print(f"The total cost of the network is {sum(self.weights)}")

    def _build_graph(self) -> None:
        self.graph = [
            [0 for _ in range(self.vertices)]
            for _ in range(self.vertices)
        ]

        # build adjacency matrix
        for u,v,w in self.edges:
            # python idx starts at zero
            self.graph[u-1][v-1] = w

            # the adjacency matrix is symmetric
            self.graph[v-1][u-1] = w
