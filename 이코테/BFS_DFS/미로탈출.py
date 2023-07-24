

"""
5 6
101010
111111
000001
111111
111111

"""

"""
책풀이 BFS
"""
# from collections import deque
# n, m = map(int, input().split())
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))
# def BFS(x, y):
#     queue = deque()
#     queue.append((x,y))
#
#     while queue:
#         x ,y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 벗어난 경우는 무시
#             if nx <0 or ny<0 or nx >=n or ny >=m:
#                 continue
#             # 벽인 경우 무시
#             if graph[nx][ny]==0:
#                 continue
#             # 노드를 처음 방문하는 경우 최단 거리 기록
#             if graph[nx][ny]==1:
#                 graph[nx][ny] = graph[x][y]+1
#                 queue.append((nx, ny))
#     # 최종값 반환
#     return graph[n-1][m-1]
#
# print(BFS(0,0))







# def DFS(x, y, n, m):
#     # graph[x][y] += 1 #계속 1+=1이기 때문에 2가됨... 으으으으음
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if nx>=0 and ny>=0 and nx<n and ny<m and graph[nx][ny]==1:
#             graph[nx][ny]= graph[x][y]+1 #상하좌우값 = 이전값+1
#             DFS(nx, ny, n, m)
#         elif nx == n-1 and ny==m-1:
#             break
#
# n, m = map(int, input().split())
# graph=[]
# for i in range(n):
#     graph.append(list(map(int, input())))
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# # 1발견 까지는 좋은데 최단거리 or 막혀있는 경우는 어떻게 배제시킬 것인가 =>  1씩 증가값을 매기자
# for i in range(n):
#     for j in range(m):
#         if graph[i][j]==1:
#             DFS(i, j, n, m)
# print(graph[i][j])


"""
테케 2,4번 에러
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def DFS(x, y, n, m, graph):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx>=0 and ny>=0 and nx<n and ny<m and graph[nx][ny]==1:
            graph[nx][ny]= graph[x][y]+1
            DFS(nx, ny, n, m, graph)
        elif nx == n-1 and ny==m-1:
            break
def solution(n, m, graph):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                DFS(i, j, n, m, graph)
    return graph[i][j]

print(solution(4,6,[[1,1,0,1,1,0],[1,1,0,1,1,0],[1,1,1,1,1,1],[1,1,1,1,0,1]])) #ex2
print(solution(4,6,[[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]])) #ex1