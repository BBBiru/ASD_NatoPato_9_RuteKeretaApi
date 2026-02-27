class Node:
    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe  # "stasiun" atau "rel"

    def __repr__(self):
        return f"{self.nama} ({self.tipe})"


class RailwayGraph:
    def __init__(self):
        self.nodes = {}
        self.adjacency = {}

    def add_node(self, nama, tipe):
        node = Node(nama, tipe)
        self.nodes[nama] = node
        self.adjacency[nama] = []

    def add_edge(self, node1, node2):
        self.adjacency[node1].append(node2)
        self.adjacency[node2].append(node1)  # karena rel dua arah

    def display(self):
        for node in self.adjacency:
            print(f"{self.nodes[node]} -> {self.adjacency[node]}")

    def bfs(self, start):
        from collections import deque
        visited = set()
        queue = deque([start])

        print("\nTraversal BFS:")
        while queue:
            current = queue.popleft()
            if current not in visited:
                print(self.nodes[current])
                visited.add(current)
                for neighbor in self.adjacency[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)


# ======================
# CONTOH PENGGUNAAN
# ======================

graph = RailwayGraph()

# Tambah stasiun
graph.add_node("Stasiun A", "stasiun")
graph.add_node("Stasiun B", "stasiun")
graph.add_node("Stasiun C", "stasiun")

# Tambah rel
graph.add_node("Rel 1", "rel")
graph.add_node("Rel 2", "rel")

# Hubungkan jalur
graph.add_edge("Stasiun A", "Rel 1")
graph.add_edge("Rel 1", "Stasiun B")
graph.add_edge("Stasiun B", "Rel 2")
graph.add_edge("Rel 2", "Stasiun C")

# Tampilkan graph
graph.display()

# Traversal
graph.bfs("Stasiun A")