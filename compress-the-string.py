# Sample Input: '1222311'
# Sample Output: (1, 1) (3, 2) (1, 3) (2, 1)

import itertools

S = list(map(int, input()))

for i, j in itertools.groupby(S):
    b = []
    b.append(len(list(j)))
    b.append(i)
    print(tuple(b), end=' ')
