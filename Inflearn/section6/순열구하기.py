
"""
순열 구하기
"""
def DFS(L):
    global cnt
    if L==m:
        for j in range(L):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0: #체크안되면
                ch[i]=1 #체크해주기
                res[L]=i #출력리스트 저장
                DFS(L+1) #다음 레벨
                ch[i]=0 #호출후 초기화

n, m = map(int, input().split())
cnt=0
ch=[0]*(n+1)
res=[0]*m
DFS(0)
print(cnt)