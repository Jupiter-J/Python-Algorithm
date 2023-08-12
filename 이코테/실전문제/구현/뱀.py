

n = int(input())
k = int(input())
graph = [[0]*n for _ in range(n+1)]

# 사과는 1표시
for _ in range(k):
    a,b = map(int, input().split())
    graph[a][b]=1

# 뱀
t = int(input())
snake = []
for _ in range(t):
    x,y = map(str, input().split())
    snake.append((int(x),y))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]



