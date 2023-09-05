


"""
동전 분배 하기
7
8
9
11
12
23
15
17

coin = [8,9,11,12,23,15,17]
"""

def DFS(L):
    global res
    if L==n:
        cha=max(money)-min(money)
        if cha<res:
            tmp=set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3:
                res=cha
    else:
        for i in range(3):
            money[i]+=coin[L]
            DFS(L+1)
            money[i]-=coin[L]

n = int(input())
money = [0]*3
res = 1e9
coin = [int(input()) for _ in range(n)]
DFS(0)
print(res)