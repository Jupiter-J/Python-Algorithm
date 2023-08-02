
"""
5
5 3 7 2 3
3 7 1 6 1
7 2 5 3 4
4 3 6 4 1
8 7 3 5 2
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 가장자리 0 초기화
graph.insert(0, [0]*n) #위 행추가
graph.append([0]*n)  #아래 행추가
for x in graph:
    x.insert(0,0) #왼쪽 가장자리 추가
    x.append(0) #오른쪽 가장자리 추가

cnt=0
for i in range(1, n+1):
    for j in range(1, n+1):
        """
        상하좌우 봉우리중 현재값 graph[i][j]보다 큰지 비교
        상하좌우 = graph[nx][ny]
        상하좌우 = graph[i+dx[k][j+dy[k]] 4바퀴 회전(for k in range(4))
        """
        if all(graph[i][j]> graph[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)

