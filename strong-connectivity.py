# Найти в заданном орграфе количество и состав сильно
# связных компонент с помощью поиска в глубину

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

def reversed_edge(edge):
    return Edge(edge.to, edge.frm)

def adjacent_nodes(node, edges):
    res = []
    for edge in edges:
        if edge.frm == node:
            res.append(edge.to)
        # elif edge.to == node:
        #     res.append(edge.frm)
    return res

def any_unused_left(nodes):
    for node in nodes:
        if node.state == 0:
            return True
    return False

nodes = []
nodes_sorted = []
edges = []
edges_tr = []

for i in range(8):
    node = Node(i)
    nodes.append(node)

edges.append(Edge(nodes[0], nodes[1]))
edges.append(Edge(nodes[4], nodes[0]))
edges.append(Edge(nodes[4], nodes[5]))
edges.append(Edge(nodes[1], nodes[4]))
edges.append(Edge(nodes[1], nodes[5]))
edges.append(Edge(nodes[1], nodes[2]))
edges.append(Edge(nodes[5], nodes[6]))
edges.append(Edge(nodes[6], nodes[5]))
edges.append(Edge(nodes[2], nodes[6]))
edges.append(Edge(nodes[2], nodes[3]))
edges.append(Edge(nodes[3], nodes[2]))
edges.append(Edge(nodes[3], nodes[7]))
edges.append(Edge(nodes[7], nodes[3]))
edges.append(Edge(nodes[7], nodes[6]))

for edge in edges:
    edges_tr.append(reversed_edge(edge))

def dfs1(node):
    node.state = 2
    for adj in adjacent_nodes(node, edges):
        if adj.state == 0:
            dfs1(adj)
    nodes_sorted.append(node)

component = []
def dfs2(node):
    node.state = 2
    component.append(node)
    for adj in adjacent_nodes(node, edges_tr):
        if adj.state == 0:
            dfs2(adj)

for node in nodes:
    if (node.state == 0):
        dfs1(node)

for node in nodes:
    node.state = 0

for node in reversed(nodes_sorted):
    if (node.state == 0):
        dfs2(node)
        print(", ".join(map(str, component)))
        component.clear()