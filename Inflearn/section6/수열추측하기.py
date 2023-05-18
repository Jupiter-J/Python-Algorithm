
"""
수열 추측하기
"""

# def DFS(L, sum):
#     if L==n and sum==f:
#         for x in p:
#             print(x, end=' ')
#         print()
#     else:
#         for i in range(1, n+1):
#             if ch[i]==0:
#                 p[L]=i
#                 ch[i]=1
#                 p[L]=i
#                 DFS(L+1, sum+(p[L]*b[L]))
#                 ch[i]=0
#
# n, f = map(int, input().split())
# p=[0]*n #순열 만들기
# b=[1]*n #초기화
# ch=[0]*(n+1) #중복방지
# for i in range(1, n):
#     b[i]=b[i-1]*(n-i)/i
# for x in b:
#     print(x, end=' ')
# DFS(0,0)