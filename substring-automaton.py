edges = [] # переходы из состояния i
link = [] # родитель i в суффиксном дереве
length = [] # наибольшая длина строки в i-м классе

firstpos = []

s = "abcadabcda"
edges.append(dict())
link.append(-1)
length.append(0)
last = 0 # индекс класса эквивалентности строки
firstpos.append(-1)

for i in range(len(s)):
    edges.append(dict())
    length.append(i+1)
    link.append(0)
    firstpos.append(length[i])
    r = len(edges) - 1

    p = last
    while (p>=0 and not (s[i] in edges[p])):
        edges[p][s[i]] = r
        p = link[p]
    if p != -1:
        q = edges[p][s[i]]
        if (length[p] + 1 == length[q]):
            link[r] = q
        else:
            edges.append(edges[q].copy())
            length.append(length[p] + 1)
            link.append(link[q])
            firstpos.append(firstpos[q])
            qq = len(edges) - 1
            link[q] = qq
            link[r] = qq
            while (p >= 0 and edges[p][s[i]] == q):
                edges[p][s[i]] = qq
                p = link[p]
    last = r

terminals = []
p = last
while p > 0:
    terminals.append(p)
    p = link[p]

w = "abcd"
ok = True
n = 0
for i in range(len(w)):
    if not (w[i] in edges[n]):
        ok = False
        break
    n = edges[n][w[i]]

# print(n)
# print(ok)
print(firstpos[n]-len(w)+1)

# print("edges")
# for i in range(len(edges)):
#     print(i, edges[i])
# print("link")
# for i in range(len(link)):
#     print(i, link[i])
# print("length")
# for i in range(len(length)):
#     print(i, length[i])