
"""
수들의 조합
"""

# def DFS(L, s, sum):
#     global cnt
#     if L==k:
#         if sum%m==0:
#             cnt+=1
#     else:
#         for i in range(s, n):
#             DFS(L+1, i+1, sum+a[i])
#
# n,k = map(int, input().split())
# a = list(map(int, input().split()))
# m = int(input())
# cnt=0
# DFS(0,0,0)


"""
복습
겹치지 않는 경우의수 구하기 
"""

# def DFS(L, s, sum):
#     global cnt
#     if L==k:
#         if sum%m==0:
#             cnt+=1
#     else:
#         for i in range(s, n): # 0 ~ n-1까지만 돌면 됨으로
#             DFS(L+1, i+1, sum+a[i])
#
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# m = int(input())
# cnt=0
# DFS(0,0,0)
# print(cnt)


def DFS(L, s, sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s, n):
            DFS(L+1, i+1, sum+a[i])

n, k = map(int, input().split())
a = list(map(int, input().split()))
m = int(input())
cnt=0
DFS(0, 0, 0)
print(cnt)