

"""
노드와 간선의 집합 = 그래프
방향이 설정된 간선 = 방향그래프
간선에 값까지 있을 경우 = 가중치 방향 그래프

무방향 그래프는 행열 모두 똑같이 체크
"""

# n 노드 갯수,  m 간선 갯수
# g 인접 행렬
n, m = map(int, input().split())
g= [[0]*(n+1) for _ in range(n+1)]

"""
무방향 인접행렬
m개의 간선의 정보가 들어온다 
==> 노드가 갈 수 있는 정보를 알려줌 
"""
for i in range(m):
    a, b= map(int, input().split())
    g[a][b]=1
    g[b][a]=1

for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()