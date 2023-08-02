
"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
3
2 0 3
5 1 2
3 1 4
"""

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

# 리스트로 받지말고 바로 변수로 받으면서 코드짬
# change = [list(map(int, input().split())) for _ in range(m)]

# 회전 배치
for i in range(m):
    h, t, k = map(int, input().split())
    if t==0:
        for _ in range(k):
            graph[h-1].append(graph[h-1].pop(0))
    else:
        for _ in range(k):
            graph[h-1].insert(0,graph[h-1].pop())


# 모래시계 위치 합
lt=0
rt=n-1
answer=0
for i in range(n):
    for j in range(lt, rt+1):
        answer+=graph[i][j]
    if i<n//2:
        lt+=1
        rt-=1
    else:
        lt-=1
        rt+=1

print(answer)

