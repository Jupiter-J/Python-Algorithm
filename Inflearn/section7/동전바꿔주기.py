
# def DFS(L, sum):
#     global cnt
#     if sum>t:
#         return
#     if L==k:
#         if sum==t:
#             cnt+=1
#     else:
#         for i in range(cn[L]+1):
#             DFS(L+1, sum+(cp[L]*i))
#
# t = int(input())
# k = int(input())
# cp = list()
# cn = list()
# for i in range(k):
#     p, n = map(int, input().split())
#     cp.append(p) #종류
#     cn.append(n) #갯수
# cnt=0
# DFS(0, 0)
# print(cnt)


def DFS(L, sum):
    global cnt
    if sum>t:
        return
    if L==k:
        if sum==t:
            cnt+=1
    else:
        for i in range(n[L]+1):
            DFS(L+1, sum+p[L]*i)

t = int(input())
k = int(input())
p = list()
n = list()
for i in range(k):
    a, b = map(int, input().split())
    p.append(a) #동전금액
    n.append(b) #갯수
cnt=0
DFS(0,0)
print(cnt)