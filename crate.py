crates = [5, 8, 15, 9, 20]
X = [8, 5, 1, 8, 5, 6, 4, 10, 5]

crates.sort(reverse=True)
X.sort(reverse=True)

for c in range(len(crates)):
    s_sum = 0
    subset = []
    for i in range(len(X)):
        if X[i] is None:
            continue
        el = X[i]
        if s_sum + el <= crates[c]:
            s_sum += el
            subset.append(el)
            X[i] = None
    print(crates[c], subset)

for x in X:
    if x is not None:
        print("Impossible")
        break