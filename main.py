

import math


def toBytes(input_path: str):
    a, m = [], []

    f = open(input_path) # TODO: write original file name to byte array as first bytes (create header)
    for l in f:
        for c in l:
            a.append(ord(c))
        for i in a:
            m.append(int(bin(i)[2:]))

    return m

def toTextFile(bin: list, output_path: str):
    l = []
    m = ""

    for i in bin:
        b = 0
        c = 0
        k = int(math.log10(i))+1
        for j in range(k):
            b = ((i % 10) * (2 ** j))
            i = i // 10
            c = c + b
        l.append(c)
    for x in l:
        m = m + chr(x)
    
    f = open(output_path, "w")
    for s in m:
        f.write(s)
    f.close()

print(toBytes("input_large.txt"))
toTextFile(toBytes("input_large.txt"), "output.txt")