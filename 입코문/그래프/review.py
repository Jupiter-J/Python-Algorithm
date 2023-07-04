


"""
컴퓨터 개수
"""
## 1. 인접행렬
# cnt=0
# def DFS(v, graph, ch, n):
#     global cnt
#     cnt+=1
#     ch[v]=1
#     for i in range(1, n+1):
#         if graph[v][i]==1 and ch[i]==0:
#             DFS(i, graph, ch, n)
#
# def solution(n, edges):
#     global cnt
#     cnt=0
#     ch=[0]*(n+1)
#     graph = [[0]*(n+1) for _ in range(n+1)]
#     for [x,y] in edges:
#         graph[x][y]=1
#         graph[y][x]=1
#     DFS(1, graph, ch, n)
#     return n-cnt

# ## 인접리스트
# answer=0
# def DFS(v, graph, ch, n):
#     global answer
#     answer+=1
#     ch[v]=1
#     for i in graph[v]:
#         if ch[i]==0:
#             DFS(i, graph, ch, n)
# def solution(n, edges):
#     global answer
#     answer = 0
#     ch = [0]*(n+1)
#     graph = [[]for _ in range(n+1)]
#     for x,y in edges:
#         graph[x].append(y)
#         graph[y].append(x)
#     DFS(1, graph, ch, n)
#     return n - answer
#
# print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))

"""
동아리 개수
"""
answer = 0
def DFS(v, ch, graph, n):
    global answer
    ch[v]=1
    for nv in graph[v]:
        if ch[nv]==0:
            DFS(nv, ch, graph, n)
def solution(n, edge):
    global answer
    answer = 0
    ch = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    # 영역구하기
    for i in range(1, n+1):
        if ch[i]==0:
            answer +=1
            DFS(i, ch, graph, n)
    return answer

print(solution(10, [[1, 2], [2, 3], [1, 4], [1, 5], [6, 8], [7, 8], [9, 10]]))