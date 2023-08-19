
# from itertools import permutations
# n, m = map(int, input().split())
# arr = list(range(1, n+1))
# print(list(permutations(arr, m)))

def DFS(v):
    global cnt
    if v==m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i]==0: #빈것을 확인
                ch[i]=1 #해당값을 1로 사용했다 표시
                res[v]=i #값 집어 넣기
                DFS(v+1)
                ch[i]=0 # 처음으로 돌아왔기 때문에 0으로 초기화

n, m = map(int, input().split())
res = [0]*n
ch=[0]*(n+1)
cnt = 0
DFS(0)
