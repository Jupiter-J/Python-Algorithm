
"""
조합구하기
"""

# def DFS(L,s):
#     global cnt
#     if L==m:
#         for j in range(L):
#             print(res[j], end=' ')
#         cnt+=1
#         print()
#     else:
#         for i in range(s, n+1):
#             res[L]=i
#             DFS(L+1, i+1)
#
# n, m = map(int, input().split())
# res=[0]*(n+1)
# cnt=0
# DFS(0,1)
# print(cnt)

# 중복 허용 없이,
# def DFS(L,v):
#     global cnt
#     if L==m:
#         for j in range(m):
#             print(res[j], end=' ')
#             cnt+=1
#         print()
#     else:
#         for i in range(v, n+1):
#             res[L]=i
#             DFS(L+1, i+1)
#
# n,m=map(int, input().split())
# res=[0]*m
# cnt=0
# DFS(0,1)
# print(cnt)

"""
복습
"""

# def DFS(L, k):
#     global cnt
#     if L==m:
#         for j in range(m):
#             print(res[j], end=' ')
#         print()
#         cnt+=1
#     else:
#         for i in range(k, n+1):
#             res[L]=i
#             DFS(L+1, i+1)
#
# n, m =  map(int, input().split())
# res=[0]*m
# cnt=0
# DFS(0,1)
# print(cnt)


def DFS(L, v):
    global cnt
    if L==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(v, n+1):
            res[L]=i
            DFS(L+1, i+1)

n, m = map(int, input().split())
res=[0]*m
cnt=0
DFS(0,1)
print(cnt)