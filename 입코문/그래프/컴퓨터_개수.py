
"""
인접행렬
"""
# cnt=0
# def DFS(v, graph, ch, n):
#     global cnt
#     ch[v]=1
#     cnt +=1 #호출한 횟수 = 컴퓨터 갯수
#     for i in range(1, n+1):
#         if graph[v][i]==1 and ch[i]==0: #v와 연결된 i & 방문안한 곳
#             DFS(i, graph, ch, n)#이동해야할곳i, 호출
# def solution(n, edges):
#     global cnt
#     ch = [0] * (n + 1)
#     graph = [[0]*(n+1) for _ in range(n+1)] #이차원 배열 - 인접행렬 (무방향그래프)
#     for [a,b] in edges:
#         graph[a][b]=1
#         graph[b][a]=1
#     cnt=0
#     DFS(1, graph, ch, n) #1번부터 출발, 그래프, 체크, 컴퓨터
#     return n-cnt #전체갯수에서 서버수 제외


# answer=0
# def DFS(v, graph, ch, n):
#     global answer
#     ch[v]=1
#     answer+=1
#     for i in range(1, n+1):
#         if graph[v][i]==1 and ch[i]==0:
#             DFS(i, graph, ch, n)
# def solution(n, edges):
#     global answer
#     ch=[0]*(n+1)
#     #인접행렬 그래프만들기
#     graph=[[0]*(n+1) for _ in range(n+1)]
#     for [x,y] in edges:
#         graph[x][y]=1
#         graph[y][x]=1
#     answer = 0
#     DFS(1, graph, ch, n)
#     return n-answer

"""
인접리스트 - 이차원 배열 활용
"""
cnt=0
def DFS(v, graph, ch, n):
    global cnt
    ch[v]=2
    cnt +=1
    for nv in graph[v]: #[v]=key값
        if ch[nv]==0:
            DFS(nv, graph, ch, n)

def solution(n, edges):
    global cnt
    ch=[0]*(n+1)
    graph = [[] for _ in range(n+1)] # [[], [], [], [], [], [], [], [], [], [], [], []]
    for [a,b] in edges:  # [[], [2, 4], [1, 3], [2], [1, 5], [4, 6], [5], [8, 10], [7, 9], [8], [7, 11], [10]]
        graph[a].append(b)
        graph[b].append(a)
    cnt = 0
    DFS(1, graph, ch, n)
    return n - cnt


print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
# print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
# print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
# print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))