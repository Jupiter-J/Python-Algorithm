

"""
가중치 방향 그래프
"""

# 노드 & 간선 입력 받기
n, m = map(int, input().split())
g = [[0]*(n+1) for _ in range(n+1)]

# 간선 정보 받기
for i in range(m):
    a, b, c = map(int, input().split())
    #가중치 "방향" 그래프이기 때문에 한번만 작성
    g[a][b]=c

# 출력하기 위해
for i in range(1, n+1):
    for j in range(1, n+1):
        print(g[i][j], end=' ')
    print()