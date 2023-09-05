



def DFS(L, sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else:
        if L+t[L]<=n+1: #상담기간 제한
            DFS(L+t[L], sum+p[L]) #(현재날짜+다음상담기간, 금액 누적)
        DFS(L+1, sum)

n = int(input())
t = []
p = []
for i in range(n):
    a, b= map(int, input().split())
    t.append(a)
    p.append(b)

res = -1e9
t.insert(0,0) #인덱스를 날짜로 하기 위해서 0 넣기
p.insert(0,0)