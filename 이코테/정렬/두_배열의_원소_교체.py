
"""

5 3
1 2 5 4 3
5 5 6 6 5
"""

from collections import deque
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
a = deque(a)
b = deque(b)
while k>0:
    k-=1
    a.popleft()
    a.append(b.popleft())

print(sum(a))

