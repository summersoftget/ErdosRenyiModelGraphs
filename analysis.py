from graph import Graph
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()

        for neighbor in graph.adj[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def count_components(graph):
    visited = set()
    count = 0

    for node in range(graph.n):
        if node not in visited:
            bfs(graph, node, visited)
            count += 1
    
    return count

def is_connected(graph):
    return count_components(graph) == 1

def average_degree(graph):
    total = sum(len(graph.neighbors(i)) for i in range(graph.n))
    return total/graph.n


def largest_component_size(graph):
    visited = set()
    max_size = 0

    for node in range(graph.n):
        if node not in visited:
            size = 0
            stack = [node]
            visited.add(node)

            while stack:
                u = stack.pop()
                size += 1

                for v in graph.adj[u]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)

            max_size = max(max_size, size)

    return max_size