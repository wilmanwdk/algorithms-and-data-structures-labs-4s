# Найти в заданном графе кратчайшие пути из заданной вершины
# до всех остальных вершин с помощью поиска в ширину

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

nodes = []
edges = []

Q = []

for i in range(ord('A'), ord('J') + 1):
    node = Node(chr(i))
    nodes.append(node)

edges.append(Edge(nodes[0], nodes[1]))
edges.append(Edge(nodes[1], nodes[2]))
edges.append(Edge(nodes[2], nodes[3]))
edges.append(Edge(nodes[3], nodes[4]))
edges.append(Edge(nodes[0], nodes[9]))
edges.append(Edge(nodes[9], nodes[4]))
edges.append(Edge(nodes[0], nodes[5]))
edges.append(Edge(nodes[5], nodes[6]))
edges.append(Edge(nodes[5], nodes[7]))
edges.append(Edge(nodes[7], nodes[8]))
edges.append(Edge(nodes[8], nodes[9]))

nodes[0].distance = 0
Q.append(nodes[0])

while len(Q) > 0:
    current = Q.pop(0)
    for adjacent in adjacent_nodes(current, edges):
        if adjacent.state == 0:
            adjacent.state = 1
            adjacent.parent = current
            adjacent.distance = current.distance + 1
            Q.append(adjacent)
    current.state = 2

print("=== 1 ===")
for node in nodes:
    print(f"{node}: {node.distance}")
print()

# Найти в заданном графе количество и состав компонент связности
# с помощью поиска в ширину
def any_unused_left(nodes):
    for node in nodes:
        if node.state == 0:
            return True
    return False

nodes = []
edges = []
components = []

Q = []

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

component = []
while any_unused_left(nodes):
    root = None
    for node in nodes:
        if node.state == 0:
            root = node
            break

    Q.append(root)

    while len(Q) > 0:
        current = Q.pop(0)
        component.append(current)
        for adjacent in adjacent_nodes(current, edges):
            if adjacent.state == 0:
                adjacent.state = 1
                adjacent.parent = current
                Q.append(adjacent)
        current.state = 2
    components.append(component)
    component = []

print("=== 2 ===")
for component in components:
    print(", ".join(map(str, component)))