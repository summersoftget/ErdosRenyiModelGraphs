import random
from graph import Graph

def generate_gnp(n, p):
    g = Graph(n)

    for i in range(n):
        for j in range(i+1, n):
            if random.random() < p:
                g.add_edge(i, j)

    return g

g = generate_gnp(5, 0.5)
print(g.adj)
