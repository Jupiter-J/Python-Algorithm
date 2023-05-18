
"""
휴가
7
4 20
2 10
3 15
3 20
2 30
2 20
1 10
"""

# def DFS(L, sum):
#     global res
#     if L==n+1:
#         if sum>res:
#             res=sum
#     else:
#         if L+tp[L]<=n+1:
#             DFS(L+tp[L], sum+pp[L])
#         DFS(L+1, sum)
#
# n = int(input())
# tp = list()
# pp = list()
# for i in range(n):
#     t,p = map(int, input().split())
#     tp.append(t)
#     pp.append(p)
# res= -2147000000
# tp.insert(0,0)
# pp.insert(0,0)
# DFS(1,0)
# print(res)

def DFS(L, sum):
    global res
    if L==n+1:
        if sum >res:
            res=sum
    else:
        if L+pt[L]<=n+1:
            DFS(L+pt[L], sum+pp[L])
        DFS(L+1, sum)

n = int(input())
pt=list()
pp=list()
for i in range(n):
    t,p = map(int, input().split())
    pt.append(t)
    pp.append(p)

pt.insert(0,0)
pp.insert(0,0)
res = -2147000000

DFS(1,0)
print(res)

