def hash(s):
    p = 15791
    n = 256
    w = 1
    res = 0
    for char in s:
        res += (w*ord(char)) % p
        w = (w*n) % p
    return res

def rk_search(source, sample):
    index = 0
    n = len(source)
    m = len(sample)
    sample_hash = hash(sample)
    # print(f"sample hash ({sample}): {sample_hash}")
    print("sample hash ({}): {}".format(sample, sample_hash))
    while index+m <= n:
        source_hash = hash(source[index:index+m])
        # print(f"index: {index}, source hash ({source[index:index+m]}): {source_hash}")
        print("index: {}, source hash ({}): {}".format(index, source[index:index+m], source_hash))
        if source_hash == sample_hash:
            ok = True
            for i in range(m):
                if source[index+i] != sample[i]:
                    ok = False
                    break
            if ok:
                return index
        index += 1
    return -1

res = rk_search("ground control to major Tom", "major")

print(res)