
"""
20
3
5 3
10 2
1 5
"""
def DFS(L, sum):
    global cnt
    if sum>t:
        return
    if L==k:
        if sum==t:
            cnt+=1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L]*i))

t = int(input())
k = int(input())
cv = []
cn = []
for i in range(k):
    a, b = map(int, input().split())
    cv.append(a)
    cn.append(b)
cnt = 0
DFS(0,0)
print(cnt)