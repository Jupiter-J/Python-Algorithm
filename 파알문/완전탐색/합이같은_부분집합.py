

"""
6
1 3 5 6 7 10
"""
from itertools import combinations
import sys
input = sys.stdin.readline
def DFS(L, sum):
    if L==n:
        # 이부분을 못짰음
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+arr[L]) # 사용함
        DFS(L+1, sum) #사용하지 않고 이전값 그대로 가져감

n = int(input())
arr = list(map(int, input().split()))
total = sum(arr)
DFS(0,0)
print("NO")