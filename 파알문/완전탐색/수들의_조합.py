
"""
5 3
2 4 5 8 12
6
"""
# L:idx, s:level, sum:합
# def DFS(L,s,sum):
#     global cnt
#     if L==k:
#         if sum%m==0:
#             cnt+=1
#     else:
#         for i in range(s, n):
#             DFS(L+1, i+1, sum+arr[i])
#
# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# m = int(input())
# cnt=0
# DFS(0,0,0)
#
# print(cnt)

from itertools import combinations
n, k = map(int, input().split())
arr = list(map(int, input().split()))
m = int(input())
cnt=0

for x in combinations(arr,k):
    if sum(x)%m==0:
        cnt+=1
print(cnt)
