class Node:
    def __init__(self, label):
        self.label = label
        self.state = 0 # 0 - белый, 1 - серый, 2 - черный
        self.parent = None
        self.distance = float("inf")
        self.component = 0

    def __str__(self):
        return str(self.label)

class Edge:
    def __init__(self, frm, to, value):
        self.frm = frm
        self.to = to
        self.value = value

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

def get_components(nodes, edges):
    Q = []
    res = []
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
        res.append(component)
        component = []
    
    for node in nodes:
        node.state = 0

    return res

nodes = []
edges = []

for i in range(9):
    node = Node(i)
    nodes.append(node)

edges.append(Edge(nodes[0], nodes[1], 2))
edges.append(Edge(nodes[0], nodes[2], 1))
edges.append(Edge(nodes[0], nodes[4], 2))
edges.append(Edge(nodes[2], nodes[4], 3))
edges.append(Edge(nodes[1], nodes[3], 3))
edges.append(Edge(nodes[3], nodes[4], 4))
edges.append(Edge(nodes[3], nodes[5], 4))
edges.append(Edge(nodes[1], nodes[5], 5))

edges.append(Edge(nodes[6], nodes[7], 1))
edges.append(Edge(nodes[7], nodes[8], 2))
edges.append(Edge(nodes[6], nodes[8], 2))

edges.sort(key=lambda e: e.value)

nodes_sets = get_components(nodes, edges)

trees = []

for nodes_set in nodes_sets:
    tree_nodes = []
    tree_edges = []
    tree_nodes.append(nodes_set[0])
    while len(tree_nodes) != len(nodes_set):
        for edge in edges:
            if (edge.frm in tree_nodes) ^ (edge.to in tree_nodes): # XOR
                if edge in tree_edges:
                    continue
                if edge.frm in tree_nodes:
                    tree_nodes.append(edge.to)
                else:
                    tree_nodes.append(edge.frm)
                tree_edges.append(edge)
    trees.append(tree_edges)

for tree in trees:
    for edge in tree:
        print(f"{edge.frm} -> {edge.to}")
    print("====")