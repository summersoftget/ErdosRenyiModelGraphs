class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = {i: [] for i in range(n)}

    def add_edge(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)
            self.adj[v].append(u)
        
    def neighbors(self, u):
        return self.adj[u]
        
