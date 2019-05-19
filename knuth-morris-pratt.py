def naive_search(source, sample):
    index = 0
    n = len(source)
    m = len(sample)

    ops = 0
    while index+m <= n:
        ok = True
        for i in range(m):
            ops += 1
            if source[index+i] != sample[i]:
                ok = False
                break
        if ok:
            print(ops)
            return index
        index += 1
    print(ops)
    return -1

def kmp_table(word):
    res = [None] * (len(word)+1)
    res[0] = -1

    pos = 1
    cnd = 0

    while pos < len(word):
        if word[pos] == word[cnd]:
            res[pos] = res[cnd]
        else:
            res[pos] = cnd
            cnd = res[cnd]
            while cnd >= 0 and word[pos] != word[cnd]:
                cnd = res[cnd]
        pos += 1
        cnd += 1

    res[pos] = cnd
    return res

def kmp_search(source, sample):
    j = 0
    k = 0
    table = kmp_table(sample)

    ops = 0
    while j < len(source):
        ops += 1
        if sample[k] == source[j]:
            j += 1
            k += 1
            if k == len(sample):
                print(ops)
                return j - k
        else:
            k = table[k]
            if k < 0:
                j += 1
                k += 1
    print(ops)
    return -1

res = kmp_search("ABC ABCDAB ABCDABCDABDE", "ABCDABD")
print("res:", res)
res = naive_search("ABC ABCDAB ABCDABCDABDE", "ABCDABD")
print("res:", res)