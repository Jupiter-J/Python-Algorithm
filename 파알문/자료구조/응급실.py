
"""
5 2
60 50 70 80 90
"""
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
patient = [(idx, value) for idx, value in enumerate(list(map(int, input().split())))]
patient = deque(patient)
cnt=0
while True:
    cur = patient.popleft()
    if any(cur[1]<x[1] for x in patient):
        patient.append(cur)
    else:
        cnt+=1
        if cur[0]==m:
            print(cnt)
            break
