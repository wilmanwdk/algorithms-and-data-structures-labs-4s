edges = [] # <char,int>; edges from node i
link = [] # parent of i
length = [] # the length of the longest string in the ith class

firstpos = []

s = "abcadabcda"
edges.append(dict())
link.append(-1)
length.append(0)
last = 0 # the index of the equivalence class of the whole string
firstpos.append(-1)

for i in range(len(s)):
    # construct r (eq class)
    edges.append(dict())
    length.append(i+1)
    link.append(0)
    firstpos.append(length[i])
    r = len(edges) - 1

    # add edges to r and find p with link to q
    p = last
    while (p>=0 and not (s[i] in edges[p])):
        edges[p][s[i]] = r
        p = link[p]
    if p != -1:
        q = edges[p][s[i]]
        if (length[p] + 1 == length[q]):
            # we do not have to split q, just set the correct suffix link
            link[r] = q
        else:
            # we have to split, add q'
            edges.append(edges[q].copy()) # copy edges of q
            length.append(length[p] + 1)
            link.append(link[q]) # copy parent of q
            firstpos.append(firstpos[q])
            qq = len(edges) - 1
            # add qq as the new parent of q and r
            link[q] = qq
            link[r] = qq
            # move short classes pointing to q to point to q'
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

print(n)
print(ok)
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