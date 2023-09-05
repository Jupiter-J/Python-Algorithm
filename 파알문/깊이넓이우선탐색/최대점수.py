"""
5 20
10 5
25 12
15 8
6 3
7 4
"""

"""
1. 종료조건 잘못함
2. 비교하기 위한 부분을 생각 못함 
"""

def DFS(L, saveScore, saveTime):
    global res
    if saveTime>m:
        return
    if L==n:
        if saveScore>res:
            res=saveScore
    else:
        for i in range(n):
            DFS(L+1, saveScore+score[L], saveTime+time[L])
            DFS(L+1, saveScore, saveTime)

n, m = map(int, input().split())
score = []
time = []
for _ in range(n):
    a, b = map(int, input().split())
    score.append(a)
    time.append(b)
res = -1e9
DFS(0, 0, 0)
print(res)