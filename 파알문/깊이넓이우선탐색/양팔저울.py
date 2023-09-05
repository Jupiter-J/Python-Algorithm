


def DFS(L, sum):
    global res
    if L==n:
        if 0<sum<=s: #sum이 양수일경우 ~ 총 무게까지 // 대칭구조임으로 음수는 제외하면 된다
            res.add(sum)
    else:
        DFS(L+1, sum+g[L]) #왼쪽
        DFS(L+2, sum-g[L]) #오른쪽
        DFS(L+1, sum) #사용하지 않을 경우

n = int(input())
g= list(map(int, input().split()))
s = sum(g)
res = set() # 중복제거
DFS(0,0)
print(s-len(res))