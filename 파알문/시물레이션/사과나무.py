
"""
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
"""

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0
lt=rt=n//2
for i in range(n):
    for j in range(lt, rt+1): #변수를 사용해 열 범위 지정하기
        answer += graph[i][j]
    if i<n//2: #x축을 중앙선으로 두어 열 범위 넓히기
        lt-=1
        rt+=1
    else:      #x축을 중앙선으로 두어 열 범위 좁히기
        lt+=1
        rt-=1
print(answer)

