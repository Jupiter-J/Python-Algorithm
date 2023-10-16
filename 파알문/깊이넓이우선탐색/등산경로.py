

"""
등산경로
값을 변경되는 방식은 BFS
"""

def DFS(x,y):
    global cnt
    if x == ex and y == ey:
        cnt+=1
    else:
        for k in range(4):
            xx=x+dx[k]
            yy=y+dy[k]
            if 0<=xx<n and 0<=yy<n and ch[xx][yy]==0 and board[xx][yy]>board[x][y]:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0

n = int(input())
board = [[0]*n for _ in range(n)]
ch = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
max = -1e9
min = 1e9
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]<min:
            min=tmp[j]
            sx=i
            sy=j
        if tmp[j]>max:
            max=tmp[j]
            ex=i
            ey=j
        board[i][j]=tmp[j]
    ch[sx][sy]=1
    cnt=0
    DFS(sx, sy)
    print(cnt)
