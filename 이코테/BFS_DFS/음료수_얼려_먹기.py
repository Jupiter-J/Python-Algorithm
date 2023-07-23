"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

4 5
00110
00011
11111
00000
"""




n, m = map(int, input().split())
ice = []
for _ in range(n):
    ice.append(list(map(int, input())))
def DFS(x, y):
    # 범위가 벗어나는 경우
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    # 해당 위치를 방문하지 않았으면
    if ice[x][y]==0:
        ice[x][y]=1
        #상, 하, 좌, 우 위치 호출
        DFS(x-1, y)
        DFS(x, y -1)
        DFS(x+1, y)
        DFS(x, y+1)
        return True
    return False

answer = 0

for i in range(n):
    for j in range(m):
        if DFS(i, j) == True:
            answer +=1

print(answer)





# def DFS(x, y, ice, n, m):
#     ice[x][y]=1
#     for k in range(4):
#         nx = x+ dx[k]
#         ny = y+ dy[k]
#         if nx>=0 and ny>=0 and nx<n and ny<m and ice[nx][ny]==0:
#             DFS(nx, ny, ice, n, m)
#
# n, m = map(int, input().split())
# ice = []
# answer=0
#
# for _ in range(n):
#     ice.append(list(map(int, input())))
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# for i in range(n):
#     for j in range(m):
#         if ice[i][j]==0:
#             answer+=1
#             DFS(i, j, ice, n, m)
#
# print(answer)


