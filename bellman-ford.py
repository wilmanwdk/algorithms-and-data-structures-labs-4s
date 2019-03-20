class Node:
    def __init__(self, label):
        self.label = label
        self.distance = float("inf")

    def __str__(self):
        return str(self.label)

class Edge:
    def __init__(self, frm, to, weight):
        self.frm = frm
        self.to = to
        self.weight = weight

nodes = []
edges = []

for i in range(ord('A'), ord('F') + 1):
    node = Node(chr(i))
    nodes.append(node)

edges.append(Edge(nodes[0], nodes[1], 1))
edges.append(Edge(nodes[0], nodes[2], 1))
edges.append(Edge(nodes[5], nodes[0], 1))
edges.append(Edge(nodes[1], nodes[4], 1))
edges.append(Edge(nodes[3], nodes[2], 1))
edges.append(Edge(nodes[4], nodes[3], 1))
edges.append(Edge(nodes[5], nodes[4], 1))
edges.append(Edge(nodes[4], nodes[0], 1))

nodes[0].distance = 0

for i in range(len(nodes) - 1):
    for edge in edges:
        if edge.to.distance > edge.frm.distance + edge.weight:
            edge.to.distance = edge.frm.distance + edge.weight

print("=================")
for node in nodes:
    print(f"{node}: {node.distance}")