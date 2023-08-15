
"""
8 3
"""
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
#prince = [n for n in range(1, n+1)]
prince  = list(range(1, n+1))
prince=deque(prince)

while prince:
    for i in range(n-1):
        prince.append(prince.popleft())
    prince.popleft()
    if len(prince)==1:
        break

print(' '.join( map(str, list(prince))))