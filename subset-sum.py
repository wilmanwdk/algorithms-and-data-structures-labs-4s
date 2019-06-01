X = [3, 7, 5, 5, 6, 6, 9, 3, 3, 4, 5, 6]
s = 30
# оптимальное - 9 + 7 + 6 + 5 + 3 = 30

X.sort(reverse=True)
subset = []
s_sum = 0
while len(X) > 0:
    el = X.pop(0)
    if s_sum + el <= s:
        s_sum += el
        subset.append(el)
    
print(subset, s_sum)