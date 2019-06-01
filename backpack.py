class Node:
    def __init__(self, weight, price, next):
        self.weight = weight
        self.price = price
        self.next = next
        self.l = None
        self.r = None
        self.code = ""
    
w = [3, 4, 5, 8, 9]
p = [1, 6, 4, 7, 6]
n = 5
s = 13

def build_tree(node):
    index = node.next
    if index >= n or node.weight + w[index] > s:
        return
    node.l = Node(node.weight, node.price, index+1)
    node.r = Node(node.weight+w[index], node.price+p[index], index+1)
    build_tree(node.l)
    build_tree(node.r)

root = Node(0, 0, 0)
build_tree(root)

end_nodes = []
def traverse(node, code=""):
    if node.l is not None:
        traverse(node.l, code+"0")
    if node.r is not None:
        traverse(node.r, code+"1")
    if node.l is None and node.r is None:
        node.code = code
        end_nodes.append(node)
        print(f"weight: {node.weight}, price: {node.price}, code: {code}")

traverse(root)
res = end_nodes[0]
for i in range(1, len(end_nodes)):
    if end_nodes[i].price > res.price:
        res = end_nodes[i]
    elif end_nodes[i].price == res.price:
        if end_nodes[i].weight < res.price:
            res = end_nodes[i]

print("=========")
for i in range(len(res.code)):
    if res.code[i] == "1":
        print(f"weight: {w[i]}, price: {p[i]}")