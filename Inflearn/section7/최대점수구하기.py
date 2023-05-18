
# """
# L 문제, sum 점수, time 문제푸는데 쓴 시간
# """
# def DFS(L,sum,time):
#     global res
#     if time>m:
#         return
#     if L==n:
#         if sum>res:
#             res=sum
#     else:
#         DFS(L+1, sum+pv[L], time+pt[L])
#         DFS(L+1, sum, time)
#
# n, m = map(int, input().split())
# pv=list() #문제점수
# pt=list() #푸는시간
# for i in range(n):
#     a ,b = map(int, input().split())
#     pv.append(a)
#     pt.append(b)
# res=-2147000000
# DFS(0,0,0)
# print(res)


def DFS(L, sum, time):
    global res
    if time>m:
        return
    if L==n:
        if sum>res:
            res=sum
    else:
        DFS(L+1, sum+ps[L], time+pt[L])
        DFS(L+1, sum, time)

n, m = map(int, input().split())
ps=list()
pt=list()
for i in range(n):
    a,b = map(int, input().split())
    ps.append(a)
    pt.append(b)
res=-2147000000

DFS(0,0,0)
print(res)