from collections import defaultdict


class EmployeeGraph:
    """
    Builds a graph for Depth-first Search

    Given an integer size (number of employees) and
    a list of the relationship between them.

    If -1, means that the employee has no direct manager

    For the full problem description, please refer to:
    Problem: https://codeforces.com/problemset/problem/115/A

    Test case:

    >>> size = 5
    >>> managers = [-1,1,2,1,-1]
    >>> g = EmployeeGraph(size, managers)
    >>> g.run()
    """

    def __init__(self, size: int, managers: list ) -> None:
        self.graph = defaultdict(list)
        self.employees = list(range(1, size+1))
        self.managers = managers
        self.edges = list(zip(self.employees, self.managers))

    def add_edge(self, u:int, v:int) -> None:
        self.graph[u].append(v)

    def run(self) -> None:
        self._build_graph()

        graph_size = len(self.graph)

        print(f"The total number of groups is {graph_size}.")

    def _build_graph(self) -> None:
        for employee, manager in self.edges:
            self.add_edge(manager,employee)