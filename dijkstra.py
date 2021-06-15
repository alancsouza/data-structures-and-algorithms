"""
Dijkstra's shortest path algorithm derived from:
https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
"""

import sys

class Graph:
    def __init__(self, size: int) -> None:
        self.vertices = size
        self.graph = [
            [0 for _ in range(size)]
            for _ in range(size)
        ]

    def min_dist(self, dist, shortest_path_tree):
        min = sys.maxsize

        for v in range(self.vertices):
            if dist[v] < min and shortest_path_tree[v] == False:
                min = dist[v]
                min_idx = v

        return min_idx

    def dijkstra(self, source):
        dist = [sys.maxsize] * self.vertices

        dist[source] = 0
        shortest_path_tree = [False] * self.vertices

        for i in range(self.vertices):
            u = self.min_dist(dist, shortest_path_tree)

            shortest_path_tree[u] = True

            for v in range(self.vertices):
                if self._should_update_dist_value(
                    u,v,shortest_path_tree,dist
                ):
                    dist[v] = dist[u] + self.graph[u][v]

        self._print_solution(dist)

    def _should_update_dist_value(self, u, v, shortest_path_tree, dist):
        return (
            self.graph[u][v] > 0
            and shortest_path_tree[v] == False
            and dist[v] > dist[u] + self.graph[u][v]
        )

    def _print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.vertices):
            print(f"{node} \t {dist[node]}")
