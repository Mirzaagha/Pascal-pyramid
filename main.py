import numpy as np
e = np.ones([2, 2])
a = np.array([1])
for x in range(10):
    b = np.zeros([3+x, 3+x])
    b[1:2+x, 1:2+x] = a
    d = np.zeros([2+x, 2+x])
    s = d.shape
    for r in range(s[0]):
        for c in range(s[1]):
            d[r, c] = np.sum(b[0+c:2+c, 0+r:2+r] *e)
    print(d)
    print("\n")
    a = d
