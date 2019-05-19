def shift_table(sample):
    d = dict()
    M = len(sample)
    for char in sample:
        if char == sample[-1]:
            if sample.count(sample[-1]) == 1:
                d[char] = M - 1
            else:
                d[char] = M - sample[:-1].rfind(char) - 1
        else:
            d[char] = M - sample.rfind(char)-1
    
    return d

def bm_search(source, sample):
    k = 0
    d = shift_table(sample)
    print(d)
    N = len(source)
    M = len(sample)
    while (k < N-M):
        j = M-1
        while source[k+j]==sample[j]:
            if j == 0:
                return k
            j -= 1

        if source[k+M-1] in d:
            k += d[source[k+M-1]]
        else:
            k += M
    return -1

print(bm_search("ABC ABCDAB ABCDABCDABDE", "ABCDABD"))