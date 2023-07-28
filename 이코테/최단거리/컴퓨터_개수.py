

"""
인접리스트
"""
answer = 0
def DFS(v, graph, ch, n):
    global answer
    ch[v]=1
    answer +=1
    for i in range(1, n+1):
        if graph[v][i] == 1 and ch[i]==0:
            DFS(i, graph, ch, n)

def solution(n, edges):
    global answer
    answer=0
    ch=[0]*(n+1)
    graph = [[0]*(n+1) for _ in range(n+1)] #이차원 배열 생성
    for [x,y] in edges:
        graph[x][y]=1
        graph[y][x]=1
    DFS(1, graph, ch, n)
    return n-answer

print(solution(11, [[1, 2], [1, 4], [2, 3], [4, 5], [5, 6], [7, 8], [7, 10], [8, 9], [10, 11]]))
# print(solution(12, [[1, 2], [1, 7], [1, 8], [1, 6], [8, 11], [11, 12]]))
# print(solution(14, [[1, 6], [1, 5], [6, 7], [7, 8], [9, 8], [3, 4], [4, 14]]))
# print(solution(15, [[1, 4], [1, 5], [9, 5], [9, 6], [7, 9], [7, 14]]))