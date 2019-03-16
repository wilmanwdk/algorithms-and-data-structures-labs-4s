class Node:
    def __init__(self, label):
        self.label = label
        self.state = 0 # 0 - белый, 1 - серый, 2 - черный
        self.parent = None
        self.distance = float("inf")

    def __str__(self):
        return str(self.label)

class Edge:
    def __init__(self, frm, to):
        self.frm = frm
        self.to = to

def adjacent_nodes(node, edges):
    res = []
    for edge in edges:
        if edge.frm == node:
            res.append(edge.to)
        elif edge.to == node:
            res.append(edge.frm)
    return res

def any_unused_left(nodes):
    for node in nodes:
        if node.state == 0:
            return True
    return False

# Найти в заданном графе количество и состав компонент связности
# с помощью поиска в глубину

nodes = []
edges = []
components = []

for i in range(1, 9):
    node = Node(i)
    nodes.append(node)

edges.append(Edge(nodes[0], nodes[3]))
edges.append(Edge(nodes[0], nodes[6]))
edges.append(Edge(nodes[2], nodes[3]))
edges.append(Edge(nodes[2], nodes[6]))
edges.append(Edge(nodes[3], nodes[6]))

edges.append(Edge(nodes[1], nodes[4]))
edges.append(Edge(nodes[1], nodes[5]))
edges.append(Edge(nodes[1], nodes[7]))
edges.append(Edge(nodes[4], nodes[5]))
edges.append(Edge(nodes[4], nodes[7]))
edges.append(Edge(nodes[5], nodes[7]))

Q = []

component = []
while any_unused_left(nodes):
    root = None
    for node in nodes:
        if node.state == 0:
            root = node
            break
    Q.append(root)
    while len(Q) > 0:
        current = Q.pop()
        if current.state == 0:
            current.state = 2
            component.append(current)
            for adjacent in adjacent_nodes(current, edges):
                Q.append(adjacent)
    components.append(component)
    component = []

print("=== 1 ===")
for component in components:
    print(", ".join(map(str, component)))
print()