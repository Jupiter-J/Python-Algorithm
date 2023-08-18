
"""
중복순열 구하기
[(1, 2), (1, 3), (2, 3)]
"""


# from itertools import product
# n, m = map(int, input().split())
# arr = list(range(1,n+1))
# print(arr)
# answer = list(product(arr, repeat=2))
# print(answer) # [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

def DFS(L):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            res[L]=i
            DFS(L+1)

n, m = map(int, input().split())
res = [0]*m
cnt=0
DFS(0)
print(cnt)
