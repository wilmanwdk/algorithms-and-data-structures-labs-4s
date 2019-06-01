class Node:
    def __init__(self, number):
        self.number = number
        self.parent = None
        self.color = -1

    def __repr__(self):
        return f"{self.number}: {self.color}"

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

for i in range(5):
    nodes.append(Node(i))

edges.append(Edge(nodes[0], nodes[2]))
edges.append(Edge(nodes[0], nodes[1]))
edges.append(Edge(nodes[1], nodes[2]))
edges.append(Edge(nodes[1], nodes[3]))
edges.append(Edge(nodes[2], nodes[4]))
edges.append(Edge(nodes[3], nodes[4]))

indices = list(range(5))

color = 0
while not len(indices) == 0:
    ind_set = []
    ind_set.append(indices.pop(0))
    for i in indices:
        ok = True
        for j in ind_set:
            if nodes[i] in adjacent_nodes(nodes[j], edges):
                print(f"{i} is adjacent to {j}")
                ok = False
                break
        if ok:
            indices.remove(i)
            ind_set.append(i)
    print(ind_set)
    for i in ind_set:
        nodes[i].color = color
    color += 1

print(nodes)