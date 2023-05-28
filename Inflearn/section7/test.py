

from collections import deque
n = int(input())
dQ = deque()
dQ.append(n)

for next in (n-1, n+1, n+5):
    print(next, end=' ')
print(dQ)