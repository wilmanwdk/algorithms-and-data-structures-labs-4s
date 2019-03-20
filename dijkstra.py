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
unvisited = []
edges = []

for i in range(ord('A'), ord('F') + 1):
    node = Node(chr(i))
    nodes.append(node)
    unvisited.append(node)

edges.append(Edge(nodes[0], nodes[1], 1))
edges.append(Edge(nodes[0], nodes[2], 1))
edges.append(Edge(nodes[5], nodes[0], 1))
edges.append(Edge(nodes[1], nodes[4], 1))
edges.append(Edge(nodes[3], nodes[2], 1))
edges.append(Edge(nodes[4], nodes[3], 1))
edges.append(Edge(nodes[5], nodes[4], 1))
edges.append(Edge(nodes[4], nodes[0], 1))
    
nodes[0].distance = 0

while True:
    if len(unvisited) == 0:
        break
    current = unvisited[0]
    for node in unvisited:
        if node.distance < current.distance:
            current = node
    if current.distance == float("inf"):
        break

    current_edges = []
    for edge in edges:
        if edge.frm == current and edge.to in unvisited:
            current_edges.append(edge)

    for edge in current_edges:
        if (edge.frm.distance == float("inf")):
            new_distance = edge.weight
        else:
            new_distance = edge.frm.distance + edge.weight
        if new_distance < edge.to.distance:
            edge.to.distance = new_distance

    if current in unvisited:
        unvisited.remove(current)

print("=================")
for node in nodes:
    print(f"{node}: {node.distance}")