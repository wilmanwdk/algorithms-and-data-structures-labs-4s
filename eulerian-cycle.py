class Node:
    def __init__(self, label):
        self.label = label
        self.deg = -1
        self.state = 0

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

def dfs(node):
    node.state = 2
    for adj in adjacent_nodes(node, edges):
        if adj.state == 0:
            dfs(adj)

def edge_by_nodes(a, b, edges):
    for edge in edges:
        if (edge.frm == a and edge.to == b) or (edge.frm == b and edge.to == a):
            return edge
    return None

nodes=[]
edges=[]

n = int(input("n: "))
for i in range(n):
    nodes.append(Node(i))
adj_mat = [None] * n
for i in range(n):
    row = list(map(int, input(str(i+1)+": ").split(' ')))
    adj_mat[i] = row
    nodes[i].deg = len([x for x in row if x == 1])

for i in range(n):
    for j in range(i, n):
        if (adj_mat[i][j]==1):
            edges.append(Edge(nodes[i], nodes[j]))

# проверка на эйлеровость
ok = True
odd = 0
for node in nodes:
    if node.deg % 2 == 1:
        odd += 1
if odd > 2:
    # если количество вершин с нечетной степенью больше двух, то граф не является эйлеровым
    ok = False
for node in nodes:
    if node.deg > 0:
        dfs(node)
        break
for node in nodes:
    if node.deg > 0 and node.state == 0:
        # если количество компонент связности, содержащие ребра, больше одной, то граф не является эйлеровым
        ok = False

print(ok)

S = []
if ok:
    v = nodes[0]
    for node in nodes:
        if node.deg % 2 == 1:
            # если граф является полуэйлеровым, то алгоритм следует запускать из вершины нечетной степени 
            v = node
            break
    S.append(v)
    while not len(S) == 0:
        w = S[-1]
        for u in nodes:
            if edge_by_nodes(u, w, edges) is not None:
                # тут мы ещё не были
                S.append(u)
                print(u, w)
                edges.remove(edge_by_nodes(u, w, edges))
                break
        if w == S[-1]:
            S.pop()