
"""
양팔저
"""

def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s: #음수는 보지 않아도 된다
            res.add(sum)
    else:
        DFS(L+1, sum+G[L]) #왼쪽
        DFS(L+1, sum-G[L]) #오른쪽
        DFS(L+1, sum) #추를 사용 안함

n = int(input())
G = list(map(int, input().split()))
s = sum(G)
res=set() #중복제거
DFS(0,0)
print(s-len(res))